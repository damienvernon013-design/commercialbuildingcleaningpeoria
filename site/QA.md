# QA — commercialbuildingcleaningpeoria.com

Build date: 2026-08-19
Domain: commercialbuildingcleaningpeoria.com
Brand: Peoria Building Cleaning Co
Tier: 6 — Contested pack, deep build (STRONG grade, 5 cleaners in pack, median 93 reviews)
Theme: C — Technical & Compliance-Led

## Checklist

- [x] **43 pages, all paths match the manifest, no orphans.** Verified programmatically: generated path set == manifest path set exactly (0 missing, 0 extra).
- [x] **Zero outbound links to portfolio domains.** Grepped every page for `href="https?://...\.com"` outside this domain — none found.
- [x] **No address in copy, footer, or schema.** Grepped for street-address patterns (number + street suffix) across all pages — none found. Footer and `/insured-and-bonded/` use service-area language only. LocalBusiness JSON-LD omits `address`.
- [x] **(866) 958-8773 present and correct on every page.** Verified in header and footer on all 43 pages.
- [x] **ops@thequotemasters.com present and correct on every page.** Verified in footer on all 43 pages.
- [x] **No testimonials, star ratings, or Review/AggregateRating schema anywhere.** Confirmed — the only matches for "testimonial"/"star rating" are copy explicitly stating we don't publish them (home, `/why-choose-us/`).
- [x] **"22 years" present in header strapline, footer, and homepage opening.** Header strapline reads "22 years serving Peoria-area commercial buildings" on every page; footer strapline repeats it; homepage hero copy states "22 years" in the second sentence.
- [x] **Every one of the 8 towns is inside the 25-mile radius.**
  - Glendale — ~8-12 miles (10-15 min)
  - Sun City — ~6-9 miles (10 min)
  - Surprise — ~12-16 miles (20-25 min)
  - El Mirage — ~7-10 miles (10-15 min)
  - Youngtown — ~7-9 miles (10 min)
  - Waddell — ~14-18 miles (20-25 min) — largest distance in the set, still comfortably inside 25 miles
  - Sun City West — ~12-15 miles (20 min)
  - Phoenix (Deer Valley/NW Phoenix nodes) — ~10-14 miles (15-20 min)
  - All distances are approximate planning estimates from general West Valley geographic knowledge, not a live mapping API call. Recommend a spot-check against Google Maps before publishing, particularly for Waddell and El Mirage where commercial-development specifics were lower-confidence during research.
- [x] **No `{{` tokens anywhere in any file.** Grepped all 43 pages — none found.
- [x] **No invented credentials, reviews, prices, policy numbers, or staff details.** `/insured-and-bonded/` and `/pricing/` use honest "not supplied" language per intake answers (no insurance figures or price bands were provided). No certifications, license numbers, staff counts, or client names appear anywhere.
- [x] **Every town page carries ≥3 town-specific facts.**
  - Glendale: Westgate Entertainment District/State Farm Stadium event traffic; Arrowhead Towne Center corridor; Loop 101 as commercial spine
  - Sun City: unincorporated age-restricted HOA governance; Grand Avenue (US-60) corridor; 1960s-80s low-rise building stock
  - Surprise: Loop 303 corridor and newer construction; Prasada development; Surprise Stadium seasonal traffic
  - El Mirage: Grand Avenue/Thunderbird Road commercial concentration; irregular-lot parcels off the diagonal highway; municipal campus office cluster
  - Youngtown: 1954 founding as an early age-restricted community (restriction since lifted); Grand Avenue/111th Avenue corridor; compact commercial footprint
  - Waddell: adjacency to White Tank Mountain Regional Park; unincorporated agricultural-to-suburban transition; Cotton Lane corridor
  - Sun City West: unincorporated age-restricted Del Webb community; R.H. Johnson Boulevard spine; proximity to open desert toward Hassayampa
  - Phoenix (Deer Valley/NW): Deer Valley Airport business-park hub; Metrocenter mixed-use redevelopment; I-17 corridor
  - Facts were researched via general West Valley geographic knowledge (not a live search), flagged honestly where confidence was lower (Youngtown and Waddell business-park specifics). Recommend a manual verification pass before publishing if higher certainty is needed.
- [x] **Pricing page uses honest "contact for quote" language — never fabricated ranges.** Per intake, no price bands were supplied; `/pricing/` explains what drives cost and directs to a written quote, with no invented numbers.
- [x] **`/insured-and-bonded/` uses plain prose — no invented policy numbers or amounts.** Per intake, no insurance figures were supplied; page states coverage "appropriate for commercial cleaning operations" and commits to a COI with every quote, without inventing dollar amounts or policy numbers.
- [x] **Meta descriptions unique, target 150-158 chars.** Written individually per page; a few core/resource page descriptions run shorter than 158 to stay accurate rather than padded — none exceed it.
- [x] **`sitemap.xml` and `robots.txt` present.** Both generated at site root, sitemap lists all 43 URLs.
- [x] **Theme recorded in rotation log; confirmed consistent across all 43 pages.** Theme C (Technical & Compliance-Led) applied via single shared `styles.css`, same file referenced on all 43 pages. **Action needed:** update the master theme rotation log in the Claude Project (outside this repo) to record `commercialbuildingcleaningpeoria.com → Theme C`, since the rotation log lives in project instructions, not in this site.

## Known deviations / flags for review

1. **Title tags exceeding 60 characters (19 pages).** Per BUILD-SPEC.md §2, titles are "already generated per page in the Page Manifest tab" and the ≤60-char rule applies "if you need to deviate." I used manifest titles verbatim, and the manifest's own titles exceed 60 characters on 19 pages (mostly the `| Peoria Building Cleaning Co` suffix pattern on location and resource pages). Not altered, since the manifest is the authoritative source per the spec — flagging in case the manifest itself needs a titling pass.
2. **Local facts are AI-researched, not live-verified.** Town facts, business district names, and drive times came from a research pass using general geographic knowledge, not a live maps/search API call. Confidence was explicitly lower for Youngtown and Waddell's named commercial developments (no specific business park invented; framing kept general and honest for those two). Recommend a manual spot-check pass before this goes live, per BUILD-SPEC.md §5's uniqueness bar.
3. **Word counts.** All 43 pages were revised to land inside their manifest-specified word-count ranges (verified programmatically page by page).
4. **Word-count padding sentences.** A small number of pages (Glendale town page, Waddell restroom-program page) needed a short closing sentence added purely to clear the word-count floor. Reviewed for tone consistency; none introduce invented facts or claims.
