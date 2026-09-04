# Repository discoverability plan

## Search intent and editorial boundary

- Primary intent: Phone-number activation and rental API workflow for agents.
- Supporting terms: phone-number, sms-api, number-rental, agent-skill, rest-api.
- Reader: a developer choosing a specific agent capability, then trying to install and use it safely.
- Conversion: understand fit, follow setup, run a discovery-only prompt, and explicitly approve any paid action.

EveryNumber supplies number-order workflows. EveryMail handles email messages; EverySolve handles authorized challenge solutions. None of these skills grants permission to create accounts or bypass service rules.

The root README owns this intent. The Chinese README serves the same product in Chinese; it is not a second keyword-swapped product. Setup, workflow and examples each answer a different practical question. Do not publish near-duplicate repositories for spelling variants or unsupported capabilities.

## Publication metadata

`repository-metadata.json` holds the proposed GitHub About description, homepage and topics. These are prepared values, not evidence that GitHub has applied them. The README title and opening describe an actual task, and FAQ answers cover this skill's specific constraints.

GitHub controls its HTML title, meta description and canonical behavior; this package cannot promise arbitrary SEO tags on GitHub. `llms.txt` is a plain documentation index, not a claim of ranking or citation preference. No search-volume or difficulty dataset was available, so the keyword map is qualitative and contains no invented metrics.

## After publication

1. Inspect the public About fields, README preview, logo rendering and documentation links.
2. Confirm that the repository can be found by its exact name and that its descriptions distinguish it from adjacent EveryInfra skills.
3. Record actual GitHub traffic, referral and clone observations when available; do not turn a view into an install or paying customer.
4. Add original examples or troubleshooting notes only when supported by real, redacted evidence. Never invent success rates, testimonials or integration claims.
5. If a website landing page is later authorized, give it a distinct useful installation/use-case purpose, link to the canonical repository, and measure indexing in the owned site's Search Console. This package does not deploy that page or assert indexing.

## Editorial sources

- [GitHub: repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub: repository topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [Google: helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google: spam policies](https://developers.google.com/search/docs/essentials/spam-policies)

These sources guide structure and publication checks; they do not endorse this project or guarantee rankings. Reviewed for this preparation on 2026-09-04.

## GEO: retrieval and verifiable answers

The first README paragraph defines the product, task and interface in a complete sentence. The capability reference keeps identity, prerequisites, limits and source links together. Product-level retrieval and outcome-level research/export have distinct scopes, so a reader can choose the right tool without conflating the packages.

These changes improve clarity and traceability; they do not establish an AI citation lift. Google states that its AI search features use the same SEO foundations and do not require special AI text files or a special schema. A GitHub repository cannot configure GitHub's robots rules or add arbitrary rendered JSON-LD. Do not invent ratings, affiliations or endorsement data.

After publication, evaluate the same branded and task-level queries, keeping timestamp, engine, query, answer mention, linked source URL and failed retrievals separate. An answer mentioning EveryInfra is not a citation unless the returned source list links to the relevant page. Do not make unobserved fields zero. A prepublication baseline is not available for these new repositories, so do not claim a measured before/after uplift.

Sources: [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features); [C-SEO Bench research and code](https://github.com/parameterlab/c-seo-bench). The research reports limitations of content-manipulation methods; it is not a prediction of this repository's future rankings.
