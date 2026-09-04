# EveryNumber workflow and acceptance criteria

## Intended outcome

An availability comparison, an explicitly authorized order state or a safely delivered result. Preserve the quoted order terms and do not infer settlement merely from number allocation.

## Execution contract

1. Read GET /api/v1/sms/catalog; use GET /api/v1/sms/rental/catalog for rentals.
2. Confirm the country, product or rental term and material spending before placing an order.
3. For activation, POST /api/v1/sms/number and preserve the returned order ID and frozen quote.
4. Poll GET /api/v1/sms/code/{order_id} within an explicit time and request limit; report the actual settlement state.
5. Cancel an unused activation with POST /api/v1/sms/cancel/{order_id} only when permitted. Rental POST /api/v1/sms/rental has a distinct paid-order boundary and no cancel or renew workflow in this skill.

## Failure handling

If discovery or catalog access fails, stop before a paid action. Read required fields from the current schema instead of copying a remembered payload. Report unavailable capabilities and denied account scopes as distinct conditions. Do not broaden keys, repeatedly retry a permanent error or substitute an unrelated mechanism without disclosure.

- REST-only; availability and prices must come from current catalogs and order responses.
- Activation is settled according to the returned code-retrieval contract, while rental is charged on order.
- No automatic rental cancellation, renewal, unlimited polling or disclosure of OTPs in files or logs.

## Worked request boundaries

### Scenario 1

> Inspect current activation options for the country and product I name. Do not allocate a number.

Accepted behavior: preserve the stated scope; discover the required contract and stop at the explicit no-action boundary. Any broader operation requires new authority.

### Scenario 2

> Explain the price and settlement differences between this activation option and rental term before I choose.

Accepted behavior: preserve the stated scope; discover the required contract and stop at the explicit no-action boundary. Any broader operation requires new authority.

### Scenario 3

> For my existing authorized activation order, propose a bounded polling and unused-order cancellation plan. Do not print any received code.

Accepted behavior: preserve the stated scope; discover the required contract and stop at the explicit no-action boundary. Any broader operation requires new authority.


These are illustrative prompts, not captured API responses or claims of successful live execution. They deliberately avoid guessed JSON payloads and fabricated prices. See [prompt acceptance fixtures](../examples/acceptance.json) for the offline safety assertions.

## Result review

An availability comparison, an explicitly authorized order state or a safely delivered result. Preserve the quoted order terms and do not infer settlement merely from number allocation.

Check original results rather than relying on the agent's summary alone. Preserve response status and evidence only to the extent safe; redact personal or secret fields. If billing is absent from the response, say it is not observable there rather than inferring a charge from HTTP success.

## Related decision

EveryNumber supplies number-order workflows. EveryMail handles email messages; EverySolve handles authorized challenge solutions. None of these skills grants permission to create accounts or bypass service rules.

Return to [README](../README.md) or [setup](setup.md).
