# EveryNumber plugin

Use EveryNumber REST for authorized phone-number activation and rental. Inspect inventory, preserve order quotes, bound code polling and distinguish settlement rules.

This package contains only `everynumber`. It is a skills-only plugin: configure the approved EveryInfra service connection in the host before using it. It does not install other skills, register a new MCP server or broaden API permissions.

An availability comparison, an explicitly authorized order state or a safely delivered result. Preserve the quoted order terms and do not infer settlement merely from number allocation.

- REST-only; availability and prices must come from current catalogs and order responses.
- Activation is settled according to the returned code-retrieval contract, while rental is charged on order.
- No automatic rental cancellation, renewal, unlimited polling or disclosure of OTPs in files or logs.

Repository documentation and installation guidance accompany the source checkout. Current API documentation: https://api.everyinfra.com/docs
