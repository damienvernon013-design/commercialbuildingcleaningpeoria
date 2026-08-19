# CLAUDE.md — commercialbuildingcleaningpeoria.com

## What this project is

A static lead-generation microsite (43 pages) for Peoria Building Cleaning Co, one domain in
a larger 60-domain commercial-cleaning lead-gen portfolio. Built per the portfolio's
`60 Domain Build Specification.md` and `Instructions Claude Project.txt` (both supplied via
the Claude Project this site was originally built from — not present in this repo, but the
rules they encode are baked into the generated copy: no reviews/testimonials, no street
address, no GBP, shared portfolio phone/email, 22-years-in-business messaging).

Deployed on Vercel. Static HTML served from `site/`, two serverless Node functions in `api/`
proxy the CRM-QM API so the CRM's Bearer token never reaches the browser.

## Repo layout — do not flatten `site/` and `api/`

```
site/    static HTML output + the Python scripts that generate it
api/     Vercel serverless functions (Node, zero dependencies, native fetch)
vercel.json   outputDirectory: "site" — this is what makes site/ serve at the domain root
```

`vercel.json`'s `outputDirectory: "site"` is load-bearing. If you move HTML files around,
either keep them under `site/` or update this config — Vercel auto-detects `api/*.js` as
functions regardless of `outputDirectory`, but static file serving depends on it.

## Regenerating the site

The 43 HTML pages are generated, not hand-written. To change page copy, edit the Python
source (`content_towns.py`, `content_scenarios.py`, or the `generate_*.py` files that call
`core_page()`/`write_page()`), then re-run:

```bash
cd site
python3 -c "
import os
for root, dirs, files in os.walk('.', topdown=False):
    for f in files:
        if f == 'index.html':
            os.remove(os.path.join(root, f))
"
python3 generate_site.py
python3 generate_extras.py
rm -rf __pycache__ _pages_built.txt
```

Never hand-edit an `index.html` file directly under `site/*/` — it will be silently
overwritten the next time someone regenerates. Edit the generator source instead.

## The CRM-QM API integration

- **Never hardcode the CRM Bearer token.** It lives only as the `CRM_API_TOKEN` environment
  variable, set in the Vercel dashboard (Project Settings → Environment Variables), read via
  `process.env.CRM_API_TOKEN` in `api/submit-lead.js` and `api/get-faq.js`. Local development
  uses `.env.local` (gitignored) copied from `.env.example`.
- `api/submit-lead.js` validates form input server-side before forwarding to the CRM, and
  fails closed (`500`) if `CRM_API_TOKEN` isn't set, rather than submitting unauthenticated.
- The CRM's `push_lead` payload requires an `industry` integer code. This is currently
  hardcoded as `INDUSTRY_CODE = 23` in `api/submit-lead.js`, carried over from the sample
  payload in the CRM API doc — **this has not been confirmed as the correct code for this
  specific vertical (Commercial Building / Multi-Tenant Cleaning)**. See `HANDOFF.md` for the
  full flag. Don't assume it's correct without checking with whoever owns the CRM's industry
  taxonomy.
- `questions` and `appointments` arrays in the CRM payload are currently always sent empty —
  the site's form doesn't collect a qualifying questionnaire or appointment slots. Adding
  those is a scope change, not a bug.
- Only `utm_source` is forwarded to the CRM (that's the only UTM field the documented payload
  defines). `lead-form.js` captures all five standard UTM params client-side in case the CRM
  payload is ever extended, but don't add the other four to the CRM call without confirming
  the CRM actually has fields for them — inventing new payload keys the API doesn't document
  risks a silent rejection or silently-ignored data.

## Content rules inherited from the portfolio build (still apply to any future edits)

- No street address anywhere (copy, footer, schema). Service-area language only.
- No `Review`/`AggregateRating` schema, no testimonials, no star ratings — this is a portfolio-
  wide FTC Consumer Review Rule compliance decision, not a stylistic one. Don't add "sample"
  or "placeholder" reviews even temporarily.
- Phone `(866) 958-8773` and email `ops@thequotemasters.com` must appear on every page,
  verbatim, in header and footer — this is a deliberate shared-identifier decision across the
  60-domain portfolio (see the build spec's §5a if it's ever added to this repo). Don't swap
  in a per-domain number without checking with the client first — it's not an oversight.
- "22 years in business" must appear in the header strapline, footer, and homepage opening on
  every page. Don't extrapolate a founding story, staff counts, or growth milestones from it.
- Zero outbound links to any other domain in the portfolio, ever.

## Testing status

The CRM integration has **not been tested against the live CRM endpoint** (explicit
instruction from the client: "no testing crm"). `node --check` syntax validation was run on
both serverless functions, and the request payload shape was manually checked against the
CRM-QM API Documentation PDF. If you're picking this up next, the first live form submission
after a Vercel deploy with `CRM_API_TOKEN` set is effectively the first real test — watch the
Vercel function logs for `submit-lead:` prefixed error lines if leads aren't landing in the
CRM.
