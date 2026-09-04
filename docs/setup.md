# Install EveryNumber and configure access

This repository packages one skill, `everynumber`, as a `everynumber` plugin. It has no runtime package dependencies or sibling-repository imports. You need a compatible agent host, an EveryInfra account for authenticated operations and the appropriate product scopes. Local packaging validation is not a live service test.

## Install from the GitHub source repository

```bash
codex plugin marketplace add everyinfra/everynumber-plugin
codex plugin add everynumber@everynumber-plugin
```

For Claude Code:

```bash
claude plugin marketplace add everyinfra/everynumber-plugin
claude plugin install everynumber@everynumber-plugin
```

These are source-repository installation paths. An installable repository catalog is distinct from a listing in a host's official marketplace. No account credential or paid API operation is included in installation.

## Local Codex installation

From the root of this checkout, add this repository-local marketplace only if it is not already configured, then install the plugin:

```bash
codex plugin marketplace add .
codex plugin add everynumber@everynumber-plugin
```

These commands change your own host configuration. Review the plugin and permissions first. Start a new task after installation if the host has not picked up the new skill. The preparation process does not run these commands or replace an existing plugin.

## Local Claude Code installation

From this checkout:

```bash
claude plugin marketplace add .
claude plugin install everynumber@everynumber-plugin
```

Review the marketplace before installing. The repository also includes a Cursor plugin manifest, but it is not evidence of Cursor marketplace approval or a completed live installation. Follow the current host's supported local plugin import flow.

## Service connection

This is a **skills-only package**: it does not register another remote MCP server, create a credential or alter your account scopes. Several standalone skills can reuse one approved EveryInfra connection. Install only the capabilities you need; installing two skills does not isolate their access to the shared server.

REST operations use the base `https://api.everyinfra.com` and the `Authorization: Bearer` scheme with a key obtained from the agent's approved secret environment, not from task text. Keep request headers and credential values out of logs. Installing an MCP connection does not create Mail, Number or Proxy MCP tools: those product workflows remain REST-only here.

The first readiness check is the public catalog. This command reads availability and does not send a message, create an order or deliver a credential:

```bash
curl --fail --silent --show-error 'https://api.everyinfra.com/api/v1/sms/catalog'
```

Read the returned schema before constructing an authenticated request. No write-request payload is hard-coded here because the live catalog is authoritative.

## Readiness and first use

1. Confirm the host loaded exactly the intended skill.
2. Confirm required tool or REST catalog access without a paid operation.
3. Check current required parameters, availability, account scope and pricing where exposed.
4. Try a discovery-only prompt from the examples.
5. Authorize the exact paid or external action separately when required.

The existing EveryInfra all-in-one plugin can contain the same skill. Prefer either the bundle or the corresponding standalone skill to avoid duplicate instructions; never uninstall an existing package without reviewing what else uses it. Package separation is not a security boundary.

## Publication and compatibility

A public source repository does not establish an official marketplace listing, completed installation in every host or an end-to-end paid API test. Use the GitHub source instructions above, or the local checkout instructions for development. See the root release checklist before publishing a tagged release or archive.
