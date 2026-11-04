---
name: company-research
description: Research an organisation from its website URL and name using web search and page fetches, to establish what it does, how big it is, its employee count, its main sector, and any training programmes or frameworks it runs. Use for any company or organisation profiling request.
---

# company-research

## Instructions

### 1. Confirm identity from the website
Use `fetch_url` on the URL provided. If the homepage is thin, fetch one more page
(About, Services, Careers or Academy/Training) that the homepage links to.
Note: what the organisation does, who it serves, sectors mentioned, any size claims.
If the site does not match the name given, say so in the description.

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
