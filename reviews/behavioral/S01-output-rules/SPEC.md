# Specification: invoice CSV export

**Status:** draft; R1-R3, R6, R7 and R9 are plannable now, R4, R5 and R8 wait on open decisions
**Decision needed:** Product to resolve D1-D3, then accept this revision as the specification for I-9.
**Next owner:** Product owner
**Intent:** I-9 revision 2 (`intent.md`)

## Requirements

| ID | Requirement | Acceptance example | Evidence planned |
| --- | --- | --- | --- |
| R1 | WHEN a signed-in user requests the export THE SYSTEM SHALL return a CSV download holding every invoice of the auth-context `account_id` and no others | Account A has 3 invoices, B has 2; A exports: 3 data rows, all A | Route test through the real domain filter |
| R2 | WHEN the request carries an account identifier other than the auth-context `account_id` THE SYSTEM SHALL export no invoice of that other account | A signed in, request names B: zero B rows | Negative route test, filter not stubbed |
| R3 | WHEN the request has no valid authentication THE SYSTEM SHALL reject it through the existing authentication with no invoice data in the response | No session: existing auth rejection, no CSV body | Route test |
| R4 | WHEN the account has no invoices THE SYSTEM SHALL return a CSV holding the header row only (pending D3) | New account: 1 header row, 0 data rows | Route test |
| R5 | WHEN an invoice field has no value THE SYSTEM SHALL emit an empty cell and keep the column count (pending D2, D3) | Invoice without a due date: row has the header's cell count | Encoder test |
| R6 | WHEN the billing API fails before the response starts THE SYSTEM SHALL return an error response with no CSV file and leave the user able to retry | Billing call raises: error status, no attachment | Route test with injected billing failure |
| R7 | WHEN the billing API fails after streaming starts THE SYSTEM SHALL abort the response so the download fails instead of ending as a shorter complete file | Failure after row 1: client sees a failed download | Streaming test over a real HTTP transport; a mocked response cannot prove it |
| R8 | WHEN a field holds a comma, quote, line break or leading formula character THE SYSTEM SHALL encode it per ADR-001 (pending D1) | Description `=1+1, "x"` reads back as one text cell | Encoder round-trip test |
| R9 | WHEN a user has only a keyboard THE SYSTEM SHALL let them reach and activate the export control and reach any resulting error message | Tab to control, Enter starts download | Keyboard walkthrough or UI test; UI file not yet identified |

## Design

- Flow: export control, then the route in `src/web/export.py`, which reads `account_id` from the auth context and passes it as a plain argument to the filter in `src/domain/invoices.py`, which calls the existing billing API; the route streams the CSV.
- Account scope comes only from the auth context. The export adds no request parameter that selects an account.
- The route completes the first billing read before sending response headers, so R6 failures can carry an error status.
- CSV encoding lives in `src/web/export.py`; the domain module returns invoice records, not CSV text.
- No change to the billing API contract; existing consumers of the invoice filter keep their behavior.

## Open decisions

| ID | Decision | Recommended answer | Owner | Blocks |
| --- | --- | --- | --- | --- |
| D1 | CSV escaping and encoding rules (`ADR-001.md`) | Option B: RFC 4180 quoting plus formula neutralisation on text fields, UTF-8 | Product owner; no security owner is named in the inputs | R8 |
| D2 | Which columns the export holds, and their order | The invoice fields the existing billing API already returns to this user, in its order; no new fields | Product owner | R1 and R5 column assertions |
| D3 | What "missing" means in I-9, and what an empty export returns | Missing is a field without a value (empty cell); empty is an account without invoices (header-only file) | Product owner | R4, R5 |

## Assumptions and exclusions

- Domain modules do not import UI (Architecture owner): checked once by an import check on `src/domain/invoices.py`.
- No new vendor and no change to the pinned vendor SDK version: checked once by a dependency manifest diff; any need to change it goes to the platform team.
- Unauthenticated behavior is whatever the existing authentication already does; this change adds no new auth path.
- No new filters, formats other than CSV, scheduling or email delivery.
- The only accessibility obligation taken from the inputs is keyboard operability; no wider target is stated.
- R7 abort behavior is a proposed choice, not stated in I-9; Product may replace it at acceptance.
- No organization or project profile was supplied; no policy clause beyond I-9 and `repo-map.txt` was applied.
- The file that owns the export control is not in `repo-map.txt`; R9 cannot be mapped to a path yet.

## Record

- Spec revision: draft 1, working copy at `SPEC.md` in the fixture directory; canonical record system not identified, so this file is not declared authoritative.
- Sources: `intent.md` (I-9 rev 2, accepted by Product), `repo-map.txt` (a description, not an inspected repository), `proposed-tasks.json`.
- Skills: ai-sdlc bundle 0.3.0, `ai-sdlc-specify`, `ai-sdlc-design`, `ai-sdlc-govern` (scope check only; no operating agreement produced).
- Authorization in scope: local analysis and planning only.
- Evidence status: `not-run`. Acceptance of this spec: pending, Product owner.
- Author role: delivery agent. Observed 22 Nov 2026, Sydney time.
