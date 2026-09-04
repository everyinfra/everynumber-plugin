#!/usr/bin/env python3
"""Offline structural checks only; no API, host installation or external writes."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


def validate(root):
    errors = []
    def check(condition, message):
        if not condition:
            errors.append(message)
    def read_json(path):
        try:
            return json.loads(path.read_text())
        except (OSError, ValueError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')
            return {}
    meta = read_json(root / 'repository-metadata.json')
    name, skill = meta.get('plugin',''), meta.get('skill','')
    plugin = root / 'plugins' / name
    skillfiles = list((root/'plugins').glob('*/skills/*/SKILL.md'))
    check(len(skillfiles)==1, 'Repository must contain exactly one SKILL.md')
    check(skillfiles == [plugin/'skills'/skill/'SKILL.md'], 'Skill path mismatch')
    check(name == plugin.name and bool(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name)), 'Invalid plugin name')
    if skillfiles:
        content = skillfiles[0].read_text()
        check(content.startswith('---\n'), 'Missing skill frontmatter')
        check(f'\nname: {skill}\n' in content, 'Skill frontmatter name mismatch')
        check('\ndescription: ' in content, 'Missing skill description')
        check('Standalone package' in content, 'Missing independent connection boundary')
        check('untrusted data' in content, 'Missing untrusted response boundary')
    for relative in ['.codex-plugin/plugin.json','.claude-plugin/plugin.json','.cursor-plugin/plugin.json','plugin.json']:
        manifest = read_json(plugin/relative)
        check(manifest.get('name')==name, f'{relative}: name mismatch')
        check(manifest.get('version')==meta.get('version'), f'{relative}: version mismatch')
        check(manifest.get('description')==meta.get('description'), f'{relative}: description mismatch')
        check(manifest.get('repository')=='https://github.com/'+meta.get('repository',''), f'{relative}: repository mismatch')
        check('mcpServers' not in manifest and 'apps' not in manifest, f'{relative}: unexpected automatic connection')
        check('[TODO' not in json.dumps(manifest), f'{relative}: scaffold placeholder')
        if relative != 'plugin.json':
            check(manifest.get('skills')=='./skills/', f'{relative}: skills path mismatch')
        interface = manifest.get('interface',{})
        for field in ['composerIcon','logo','logoDark']:
            if field in interface:
                check((plugin/interface[field]).is_file(), f'Missing asset {field}')
    for relative in ['.agents/plugins/marketplace.json','.claude-plugin/marketplace.json','.cursor-plugin/marketplace.json']:
        market = read_json(root/relative)
        check(market.get('name')==meta.get('repository','').split('/')[-1], f'{relative}: marketplace mismatch')
        entries = market.get('plugins',[])
        check(len(entries)==1, f'{relative}: must list one plugin')
        if len(entries)==1:
            entry = entries[0]
            source = entry.get('source')
            if isinstance(source,dict):
                check(source.get('source')=='local', f'{relative}: unexpected source type')
                source = source.get('path')
                check(entry.get('policy')=={'installation':'AVAILABLE','authentication':'ON_INSTALL'}, 'Codex policy mismatch')
                check(bool(entry.get('category')), 'Codex category missing')
            check(source==f'./plugins/{name}', f'{relative}: source path mismatch')
            check(entry.get('name')==name, f'{relative}: entry name mismatch')
    topics = meta.get('topics',[])
    check(1<=len(topics)<=20 and len(set(topics))==len(topics), 'Invalid topic count or duplicates')
    check(all(re.fullmatch(r'[a-z0-9-]{1,50}',x) for x in topics), 'Invalid GitHub topic syntax')
    check(0<len(meta.get('description',''))<=350, 'Invalid GitHub description length')
    check(meta.get('transport') in ['mcp','rest','mixed'], 'Unknown transport')
    required = ['README.md','README.zh-CN.md','LICENSE','SECURITY.md','SUPPORT.md','CONTRIBUTING.md',
                'RELEASING.md','CHANGELOG.md','CLAUDE.md','AGENTS.md','llms.txt','docs/setup.md',
                'docs/workflow.md','docs/discoverability.md','examples/prompts.md','.github/workflows/validate.yml']
    for relative in required:
        check((root/relative).is_file() and (root/relative).stat().st_size>0, f'Missing {relative}')
    check((root/'AGENTS.md').is_symlink() and (root/'AGENTS.md').resolve()==(root/'CLAUDE.md').resolve(), 'AGENTS.md must link to CLAUDE.md')
    readme = (root/'README.md').read_text()
    check(readme.count('\n# ')==0 and readme.startswith('# '), 'README must have one H1')
    check(meta.get('readmeTitle') in readme.splitlines()[0], 'README intent title mismatch')
    check(readme.count('\n### ')>=4, 'README must include result detail and specific FAQ')
    if meta.get('transport')=='rest':
        check('REST-only' in readme, 'REST-only capability boundary missing')
    fixtures = read_json(root/'examples/acceptance.json')
    check(isinstance(fixtures,list) and len(fixtures)>=3, 'Missing acceptance fixtures')
    if isinstance(fixtures,list):
        for f in fixtures:
            check(all(f.get(x) is True for x in ['must_preserve_scope','must_discover_contract','must_not_infer_permission']), 'Fixture safety assertions missing')
            check(f.get('example_type')=='illustrative-not-live' and bool(f.get('prompt')), 'Invalid fixture')
    checked_links = 0
    json_count = 0
    for path in sorted(root.rglob('*')):
        if any(x in {'.git','__pycache__','dist'} for x in path.relative_to(root).parts) or path.is_symlink() or not path.is_file():
            continue
        if path.suffix=='.json':
            read_json(path)
            json_count+=1
        if path.suffix=='.svg':
            try:
                tree=ET.parse(path)
                check(tree.getroot().tag.endswith('svg'), f'{path.name}: not SVG')
            except ET.ParseError as exc:
                errors.append(f'{path.name}: {exc}')
        if path.suffix in {'.md','.txt'}:
            text=path.read_text()
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
                parsed=urlsplit(target.strip('<>'))
                if parsed.scheme or target.startswith('#'):
                    continue
                local=(path.parent/unquote(parsed.path)).resolve()
                check(local.is_relative_to(root.resolve()) and local.exists(), f'{path.relative_to(root)}: broken local link {target}')
                checked_links+=1
            check(not re.search(r'omggrow|apify|tikhub|root-secrets|BEGIN (?:RSA |EC )?PRIVATE KEY',text,re.I), f'{path.relative_to(root)}: private or legacy terminology')
    check(not list(plugin.rglob('.mcp.json')) and not list(plugin.rglob('.app.json')), 'Unexpected automatic service registration')
    if errors:
        print('\n'.join('ERROR: '+e for e in errors),file=sys.stderr)
        return 1
    print(f'PASS {meta["repository"]}: 1 skill, 4 manifests, 3 catalogs, {json_count} JSON files, {checked_links} local links; offline only')
    return 0


if __name__=='__main__':
    sys.exit(validate(Path(__file__).resolve().parents[1]))
