# S01 — invoice CSV export specification, draft 1

Authoritative accepted intent: **I-9 revision 2, accepted by Product**, as supplied in `intent.md`. This specification is a local draft derived from that record, not a newly accepted product decision. Raw input identities are in `input-provenance.json`. Actual repository revision, profile versions and specification acceptance are not supplied.

## Scope and constraints

Add CSV export of the signed-in user's own invoices in the existing web app. Reuse existing authentication and billing APIs. No new vendor or vendor SDK upgrade is proposed. Preserve the architecture rule that domain modules must not import UI. Product requires keyboard operability. Planning/local analysis only is authorized; no code, agent launch or publication is requested.

Auth context supplies `account_id`; use it as the account boundary, never a client-selected account ID. The supplied intent explicitly prohibits exporting another account's invoices. If this application distinguishes personal invoice visibility within one account, its existing authorization rule must also be confirmed before implementation; the fixture supplies no finer-grained rule.

## Combined behavior/design matrix

| ID | Requirement and design consequence | Acceptance scenario | Planned proof |
| --- | --- | --- | --- |
| R1 | Export only invoices authorized by authenticated account context. Web obtains trusted identity; domain filtering enforces scoped selection. | Signed-in account A with A and B invoices in the source receives only permitted A rows. | Domain/route tests with mixed-account fixtures and negative checks against B. |
| R2 | Client parameters cannot switch the authorization account. Existing authentication/denial behavior is reused. | A submits a B selector or requests export without valid auth; no B data or unauthenticated CSV is returned. | Route tests against existing auth integration; inspect actual status/error convention before finalizing assertions. |
| R3 | Reuse billing APIs and the platform-pinned SDK; introduce no vendor. | Export follows the existing supported API/SDK contract and changes no dependency/vendor configuration. | Reviewed API contract plus dependency/lockfile diff; allowed integration test approach must be selected from project policy. |
| R4 | Export valid, consistent CSV using a decided schema and escaping policy. Serialization stays in the web/formatting boundary, not domain/UI coupling. | A selected field includes delimiter, quote, newline, Unicode or a spreadsheet formula prefix. Result matches the accepted serialization/safety policy. | Round-trip/parser and exact output cases after decisions D1/D2; no current pass claim. |
| R5 | Define missing, empty and error states using existing product/API conventions. Do not leak another account's data or produce a misleading successful download. | Missing required request input, no invoices, and billing failure each produce the accepted state; retry does not broaden authorization. | Route and UI state tests after confirming conventions; error-before-stream and mid-stream failure behavior assessed. |
| R6 | The export interaction is keyboard operable with a meaningful name and understandable progress/error state. Existing authentication remains in the flow. | A keyboard user reaches and activates export, can understand failure and retry without losing the task. | Actual keyboard walkthrough and appropriate semantic/component checks once the UI entry point exists; not performed here. |
| R7 | Domain code must not import UI; it owns invoice filtering. | Domain processing is exercised without importing web/UI modules. | Dependency/import inspection and relevant domain tests; architecture decision ADR-001. |

## User/system flow

1. A signed-in user reaches an export control in the existing invoice UI. The actual UI file/route must be located; it is absent from the supplied repository map.
2. Web request handling validates inputs under existing conventions and obtains the trusted account context.
3. Domain filtering selects only permitted invoice records through the existing billing interface. Web code does not expand the result with another account's data.
4. Web serialization emits the agreed columns/dialect safely and streams the response. Determine when headers/streaming begin relative to billing/API errors so partial output is not presented as a complete success.
5. Empty/missing/error conditions use the accepted states. The initiating control and any status/retry affordance remain keyboard usable.

## Decisions and missing evidence

- **D1 — CSV policy, unresolved:** delimiter/quoting, encoding/newline, null representation and handling spreadsheet interpretation of formula-leading cells. Quoting alone and prefixing a literal character have different semantics. Product/engineering, with the relevant security owner if required, must choose based on intended consumers. No escaping rule is silently treated as accepted. Blocks final serializer behavior and its expected-output tests; domain isolation analysis can continue.
- **D2 — export fields and compatibility, unresolved:** column names/order and allowed invoice fields are not provided. Use established product/API schema if one exists and confirm intended export scope. Do not export every upstream field by default.
- **D3 — state conventions, unresolved:** inspect actual route/UI behavior for missing input, empty export, API failure and mid-stream failure. Exact HTTP codes, filenames and UI wording are proposed implementation details until confirmed.
- **D4 — repository and verification context, unavailable:** code, API shape, pagination, invoice volume, build/test commands and UI location are not supplied. The repository map is evidence of stated responsibilities, not an inspected implementation. Do not invent performance targets or API names.

## Readiness and acceptance

Drafting and unaffected planning are complete. Final specification acceptance and implementation readiness remain partial pending the material decisions and actual repository inspection. Product acceptance of I-9 revision 2 is preserved; no new Product or Architecture signature is fabricated. Source of truth remains I-9 until an owner assigns this draft an authoritative location/revision.
