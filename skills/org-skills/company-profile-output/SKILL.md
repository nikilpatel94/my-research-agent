---
name: company-profile-output
description: Format the final answer of a company research task as a strict three-field JSON object (description, employee_strength, main_sector). Use as the last step, after research is complete, whenever a company profile is the deliverable.
---

# company-profile-output

## Contract

Reply with a single JSON object and nothing else: no preamble, no markdown fences,
no extra keys.

| Field | Content |
| - | - |
| `description` | 3-5 plain sentences: what the organisation does; how big it is (revenue, offices, countries, clients, where evidenced); any work-related training programme or framework it runs. |
| `employee_strength` | Short string: a figure or range, with source type and year. `"Not found"` if unavailable. |
| `main_sector` | Short phrase naming the primary sector of operations. |

## Example

{"description": "Acme Learning Ltd designs and delivers leadership and technical training for UK utilities. It operates from three offices and serves around 120 corporate clients. It runs the Acme Capability Framework, a competency model used to structure its certified programmes.", "employee_strength": "~250 (company website, 2025)", "main_sector": "Corporate learning and development"}

## Rules
- Write in neutral third person, with no marketing language.
- Do not include URLs or citations inside the fields.
- If the evidence is weak, say so inside `description` rather than guessing.
