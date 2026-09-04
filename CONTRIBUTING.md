# Contributing to EveryNumber

Keep this repository focused on one skill and its real customer contract. Start with a reproducible issue, the intended behavior and redacted evidence. Do not include API keys, message bodies, OTPs, proxy passwords or private customer data.

Changes to `plugins/everynumber/skills/everynumber/SKILL.md` should include updated examples and acceptance criteria when behavior changes. Run `python3 scripts/validate.py` before proposing a patch. Keep all plugin manifest versions aligned and update `CHANGELOG.md` for released behavior changes.

Use the current live catalog as the capability boundary. Do not add guessed tools, unsupported fields, pricing claims or fake testimonials. Installation and execution changes need host-level checks beyond JSON validation. Publishing and production account changes require maintainer approval.

The source skill was imported from the public EveryInfra bundle at the commit recorded in `repository-metadata.json`; this repository is now intended to evolve independently. See [release guidance](RELEASING.md).
