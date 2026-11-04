---
name: company-research
description: Research an organisation from its website URL and name using web search and page fetches, to establish what it does, how big it is, its employee count, its main sector, and any training programmes or frameworks it runs. Use for any company or organisation profiling request.
---

# company-research

## Instructions

### 1. Verify the name matches the URL (gate: do this before any research)
Make one `fetch_url` call on the URL provided and nothing else. Check the page title,
headings, footer and any legal or copyright line for the organisation name.
Treat brand vs legal names, abbreviations, and a parent company or group as a match.

- **Match**: continue to step 2. Keep what the page already told you
  (what they do, who they serve, sectors, size claims) so you don't fetch it again.
- **Fetch failed or page too thin to judge**: run one `web_search` for
  `{name} {domain}`. Continue only if the results tie that domain to the organisation.
- **Mismatch** (the site belongs to a different organisation, or nothing links it
  to the name): stop here. Do no further searches. Skip to the output skill and return
  `description` stating the mismatch and what the site actually belongs to,
  with `employee_strength` and `main_sector` set to "Not found".

### 2. Search the web (budget: 6 searches maximum)
Run distinct queries, replacing `{name}` with the organisation name:

- `{name} company overview what we do`
- `{name} number of employees`
- `{name} company size revenue offices countries`
- `{name} training programme academy framework methodology`
- `{name} industry sector`

Skip any query already answered by earlier results. Use `fetch_url` on at most
2 promising results when a snippet is too thin.

### 3. Source priority
Official website > regulatory filings / annual reports > reputable press >
profile aggregators (LinkedIn, Crunchbase and similar). Prefer the most recent figure.

### 4. What to establish
- **What they do**: core products or services and customers.
- **How big**: revenue, offices, countries, clients, whichever is evidenced.
- **Employee strength**: a figure or range, with source type and year.
- **Training programme or framework**: proprietary methodologies, academies,
  certifications, learning programmes, internal frameworks. Include only what a source evidences.
- **Main sector**: the primary industry they operate in.

### 5. Rules
- Never invent figures. If a point cannot be found, write "Not found".
- If sources conflict on employee numbers, give the range and flag the conflict.
- If no training programme or framework is documented, state that explicitly.
- Stop once all five points are covered or the search budget is spent.

When research is finished, follow the `company-profile-output` skill to write the final answer.