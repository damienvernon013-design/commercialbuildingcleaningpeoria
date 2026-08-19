# Handoff — commercialbuildingcleaningpeoria.com

**Status: READY TO LAUNCH** (see caveats below — one item needs client confirmation)

## What this is

A 43-page static lead-generation microsite for Peoria Building Cleaning Co, generated from
Python build scripts, deployed to Vercel as static HTML + two serverless API functions that
proxy the CRM-QM API.

## Repo layout

```
commercialbuildingcleaningpeoria/
  site/               43 static HTML pages, styles.css, lead-form.js — this is the deployed web root
    build.py            shared HTML template helpers (header, footer, form markup)
    generate_site.py    home + 8 core pages + services hub
    generate_services.py  3 /services/{service}/ pages
    generate_areas.py   /service-areas/ hub + 8 town pages + 16 town x service pages
    generate_resources.py  5 /resources/{article}/ pages
    generate_extras.py  sitemap.xml + robots.txt
    content_towns.py    per-town facts/drive-times used by generate_areas.py
    content_scenarios.py  per-town-x-service building scenarios
    QA.md                build QA checklist from the original site build
  api/                Vercel serverless functions (Node, no framework)
    submit-lead.js       POST /api/submit-lead — receives form data from lead-form.js,
                          validates it, and forwards it to the CRM PushLead endpoint with
                          the Bearer token attached server-side
    get-faq.js            GET /api/get-faq — proxies the CRM GetFaq endpoint, cached 5 min
  vercel.json           outputDirectory: "site" so the static pages serve at the domain root
  package.json          minimal — no dependencies, Node 18+ native fetch is used
  .env.example           documents the one required env var
  .gitignore              excludes .env*, dist/, __pycache__
```

## How the contact form works now

Previously the quote form on `/contact/` and `/request-a-quote/` posted to a dead HTML
endpoint (`/request-a-quote/thank-you/`, which never existed). It's now wired end-to-end:

1. `site/lead-form.js` (loaded on every page via a `<script defer>` tag) intercepts the form
   submit, builds a JSON payload matching the CRM's expected shape, and POSTs it to
   `/api/submit-lead` — a same-origin Vercel function, not the CRM directly.
2. `api/submit-lead.js` validates the payload server-side, attaches
   `Authorization: Bearer ${process.env.CRM_API_TOKEN}`, and forwards it to
   `https://thequotemasters.com/crm_api/api.php?action=push_lead`.
3. The Bearer token never reaches the browser. It exists only as a Vercel environment
   variable, read via `process.env.CRM_API_TOKEN` at request time.

Form fields were changed from the original single `name` field to `first_name` / `last_name`
(the CRM requires them split), and a required `zip` field was added (the CRM requires it, and
it also naturally supports confirming a lead is inside the 25-mile service radius).

**Fields NOT wired up yet, because the source PDF didn't give us the data to map them
correctly:** `questions` (industry-specific questionnaire) and `appointments` (preferred
time slots) are sent as empty arrays in every submission. The CRM API accepts them; this
site just doesn't collect that data on the form. If the client wants the qualifying
questionnaire or appointment picker, that's a follow-up scope item, not something inferred
here.

## UTM tracking

`site/lead-form.js` captures `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, and
`utm_content` from the URL query string on page load and persists them to `sessionStorage`
so they survive multi-page browsing before the visitor submits the form. On submit, all five
are included in the payload to `/api/submit-lead`, but **only `utm_source` is forwarded to the
CRM**, because that's the only UTM field the CRM-QM API's `push_lead` payload documents
(`"utm_source": ""  //Define your source type text(255)`). The other four are accepted by the
function and available if the CRM payload shape is ever extended, but are currently dropped
before the CRM call rather than silently invented into fields the API doesn't define.

## Required setup before this goes live

**One manual step is required in the Vercel dashboard — this was not and cannot be done from
this session:**

1. Go to the Vercel project → Settings → Environment Variables.
2. Add `CRM_API_TOKEN` with the Bearer token value from the CRM-QM API Documentation PDF you
   provided, scoped to Production (and Preview if you want form testing on preview deploys).
3. Redeploy (or the next push will pick it up automatically).

Without this, `/api/submit-lead` and `/api/get-faq` will return `500 Server misconfiguration`
by design — the functions check for the env var and fail closed rather than silently
submitting without auth.

## Flag for the client: `industry` code

The CRM payload requires an `industry` field (an integer code). The only value we have is
`23`, taken from the sample payload in the PDF you provided — that sample wasn't confirmed as
the code specifically for "Commercial Building / Multi-Tenant Cleaning" as opposed to being a
generic example value. `api/submit-lead.js` currently hardcodes `INDUSTRY_CODE = 23`
(see the constant at the top of the file). **Confirm this is the correct industry code for
this vertical before relying on lead routing inside the CRM** — if it's wrong, leads will
still submit successfully but may get miscategorized on the CRM side. This is a one-line
change in `api/submit-lead.js` if it needs correcting.

## What was explicitly not done, per your instructions

- **No testing of the CRM integration.** You said "no testing crm" — `/api/submit-lead` has
  not been exercised against the live CRM endpoint. Node syntax was checked
  (`node --check`) and the payload shape was validated against the PDF's documented
  structure, but no live request was made. The first real test will be the first real form
  submission after deploy.
- **No `vercel` CLI usage.** You said the repo is already connected to Vercel and not to
  check via CLI. No `vercel` commands were run; deployment is expected to happen via Vercel's
  GitHub integration picking up the push to `main`.

## Placeholder / content audit

Ran a repo-wide scan for `{{ }}` template tokens, `TODO`/`FIXME`/`TBD`/`XXX` markers,
`lorem ipsum`, and generic placeholder domains (`example.com`, `your-domain`, `changeme`).
None found outside of Python f-string brace-escaping in the generator scripts themselves
(not rendered into output) and the `type="email"` HTML attribute (a false-positive match on
the word "email", not a placeholder). See `site/QA.md` for the original content QA pass
covering phone/email/address/review-schema/word-count checks across all 43 pages — those
findings still hold; nothing in this pass touched page copy.

## Secrets check before this commit

Confirmed via grep across the entire repo: the literal Bearer token value from the PDF does
not appear anywhere in tracked files. `.env` and `.env.local` are gitignored. Only
`.env.example` (with an empty value) is committed.
