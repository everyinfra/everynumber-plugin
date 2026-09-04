# EveryNumber: capability reference and evidence

EveryNumber is a standalone EveryInfra agent skill for authorized phone-number activation and rental through REST. It discovers current inventory, preserves order quotes, bounds code polling and distinguishes activation settlement from rental purchase.

## Identity

- Publisher: [EveryInfra](https://everyinfra.com).
- Organization: [everyinfra on GitHub](https://github.com/everyinfra).
- Source repository: [everyinfra/everynumber-plugin](https://github.com/everyinfra/everynumber-plugin).
- Plugin identifier: `everynumber`. Skill identifier: `everynumber`.
- Package type: one standalone agent skill, not a separate API server or account permission boundary.
- Interface used by the skill: `rest`. Mail, Number and Proxy workflows remain REST-only in these packages.

## Task and result

Use it for an authorized phone-number workflow with a specified country and product or rental term. Handle codes as secrets and respect the target service’s rules; do not use the workflow for account abuse.

An availability comparison, an explicitly authorized order state or a safely delivered result. Preserve the quoted order terms and do not infer settlement merely from number allocation.

## Preconditions

Use a compatible agent host and the service access described in [setup](setup.md). The live tool schema or REST catalog determines required inputs, supported actions, availability, limits and any exposed price. Do not infer universal platform coverage from a product name.

## Evidence behind the description

- The [packaged skill](../plugins/everynumber/skills/everynumber/SKILL.md) defines the workflow and authority boundaries.
- The [plugin manifest](../plugins/everynumber/.codex-plugin/plugin.json) declares package identity, assets and skill path. It does not automatically register a service connection.
- [Workflow acceptance criteria](workflow.md) define the expected output and failures. Examples are illustrative, not paid API test results.
- [Source metadata](../repository-metadata.json) records the original reviewed skill commit and intended repository metadata.
- [Current API documentation](https://api.everyinfra.com/docs) is the public service reference. Runtime discovery remains authoritative when an inventory, field or model changes.

## Scope distinctions

EveryNumber supplies number-order workflows. EveryMail handles email messages; EverySolve handles authorized challenge solutions. None of these skills grants permission to create accounts or bypass service rules.

No benchmark, uptime guarantee, universal availability, official marketplace approval or account-ban probability is asserted by this reference. Local package validation checks structure; production service behavior requires its own authorized verification.

Maintainer: EveryInfra. Documentation scope reviewed on 2026-09-04; this date is not a live API availability timestamp. [Return to overview](../README.md).
