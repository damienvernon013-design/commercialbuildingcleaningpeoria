#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import (
    page, write_page, header_nav, footer, quote_form_snippet,
    BRAND, PHONE, PHONE_TEL, EMAIL, HOURS, YEARS, SERVICES, TOWNS, ADJACENCY, BASE_URL
)
from content_towns import TOWN_DATA, TOWN_ORDER
from content_scenarios import SCENARIOS

pages_built = []

def record(path):
    pages_built.append(path)

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
home_body = f"""
<p class="lede" style="max-width:70ch;font-size:1.05rem;color:var(--text-muted);margin-bottom:20px;">
{YEARS} serving commercial buildings across Peoria and the West Valley. Insured and bonded.
Free quote, next-business-day response.
</p>

<div class="hero-actions" style="margin-bottom:32px;">
  <a class="btn-primary" href="/request-a-quote/">Request a Free Quote</a>
  <a class="btn-secondary" href="tel:{PHONE_TEL}">Call {PHONE}</a>
</div>

<p>Peoria Building Cleaning Co connects property managers, building engineers, and asset managers across the Peoria, Arizona area with vetted commercial cleaning crews. We coordinate common-area cleaning, multi-tenant restroom programs, and day porter coverage for office buildings, medical buildings, and mixed-use properties along the Loop 101 corridor and throughout the surrounding West Valley. {YEARS} in this market means we know which buildings need dust-focused entry care after a haboob rolls through and which need a tighter restroom rotation for a medical tenant mix.</p>

<p>Commercial buildings in the Peoria area face maintenance conditions that a generic national cleaning contract doesn't account for. Monsoon season, roughly mid-June through September, brings dust storms that leave a visible film on entry glass and lobby flooring within hours of a wind event. Summer highs that regularly clear 110 degrees put extra strain on HVAC intake grilles and accelerate exterior soiling in a way that cooler-climate buildings never deal with. And the tenant mix across our service area ranges from downtown-style multi-story office buildings near Loop 101 to single-story medical suites serving the age-restricted communities in Sun City and Sun City West, each with a different cleaning cadence that actually fits.</p>

<p>We work as the coordination layer between your building and the crews who service it. That means a single point of contact for scheduling, a written scope of work agreed before the first clean, and a response-time commitment you can hold us to, rather than a vague promise buried in a contract nobody rereads after signing.</p>

<h2>Our Services</h2>
<div class="card-grid">
"""
for slug, name in SERVICES:
    home_body += f"""  <div class="card">
    <h3>{name}</h3>
    <p>{{desc}}</p>
    <a class="card-link" href="/services/{slug}/">Learn more &rarr;</a>
  </div>
"""
service_descs = {
    "common-area-lobby-cleaning": "Lobby floors, entry glass, elevator interiors, and shared corridors kept to a standard tenants notice.",
    "multi-tenant-restroom-programs": "Scheduled restocking, disinfection, and fixture checks across shared restroom cores.",
    "day-porter-services": "On-site daytime coverage for spills, restocking, and common-area upkeep during business hours.",
}
for slug, desc in service_descs.items():
    home_body = home_body.replace("{desc}", desc, 1)

home_body += """</div>

<h2>Service Areas</h2>
<p>We serve commercial buildings within a 25-mile radius of Peoria, including:</p>
<div class="town-grid">
"""
for slug, name in TOWNS:
    home_body += f'  <a href="/service-areas/{slug}/">{name}</a>\n'
home_body += """</div>
<p><a href="/service-areas/">View all service areas &rarr;</a></p>

<h2>Why Property Managers Work With Us</h2>
<ul>
<li><strong>22 years in this market.</strong> We know the seasonal dust patterns, the monsoon-season entry care, and the building stock differences between a Sun City medical suite and a Deer Valley light-industrial building.</li>
<li><strong>Insured and bonded</strong> on every job, with a certificate of insurance included with every written quote.</li>
<li><strong>Response within one business day.</strong> Quotes and service requests submitted during business hours or after get a next-business-day reply.</li>
<li><strong>Written scope of work on every job.</strong> What's covered, how often, and what it costs is documented before the first clean, not negotiated informally after service starts.</li>
<li><strong>No fabricated trust signals.</strong> We don't publish testimonials or star ratings. Our credentials are insurance documentation, a transparent process, and a track record you can verify by calling.</li>
</ul>

<h2>Built for Property Managers, Building Engineers, and Asset Managers</h2>
<p>If you manage a single building or a regional portfolio, the friction in commercial cleaning usually isn't the cleaning itself, it's coordination: chasing a vendor for a written quote, discovering scope gaps after a tenant complains, or losing track of which building is on which schedule. We built our process to remove that friction. Every property gets an itemized scope of work broken out by service line, so you can see exactly what you're paying for and defend it at CAM reconciliation without guessing.</p>

<h2>What Makes This Market Different</h2>
<p>The Peoria area sits within the West Valley's broader commercial corridor, where building stock ranges from newer glass-and-concrete construction near Loop 101 and Loop 303 to older, single-story medical buildings in the age-restricted communities of Sun City and Sun City West. A vendor who treats every building the same, applying a downtown-office cleaning template to a Sun City medical suite or ignoring the dust exposure a Waddell building near White Tank Mountain Regional Park actually deals with, ends up either overcharging for coverage a building doesn't need or under-delivering on the coverage it does.</p>

<p>Ready to see pricing for your building? <a href="/request-a-quote/">Request a free quote</a> or call {PHONE} during our {HOURS} hours.</p>
"""
canonical = "/"
title = "Commercial Building Cleaning Peoria, AZ | Free Quote Same Day"
desc = "Free quote in 60 seconds. Insured crews serving Peoria, AZ commercial buildings for 22 years. Common area, restroom, and day porter service."
write_page(canonical, page(title, desc, canonical,
    "Commercial Building Cleaning in Peoria, Arizona", home_body))
record(canonical)

# ---------------------------------------------------------------------------
# CORE PAGES
# ---------------------------------------------------------------------------

def core_page(path, title, desc, h1, body):
    write_page(path, page(title, desc, path, h1, body))
    record(path)

core_page(
    "/about/",
    f"About {BRAND} | Commercial Building Cleaning in Peoria, AZ",
    f"About {BRAND}: {YEARS} coordinating insured commercial cleaning crews for Peoria, AZ buildings. Call {PHONE} for a free quote.",
    f"About {BRAND}",
    f"""
<p>{BRAND} has spent {YEARS} coordinating commercial cleaning coverage for office buildings, medical buildings, and mixed-use properties across Peoria, Arizona and the surrounding West Valley. We work with property managers, building engineers, and REIT asset managers who need a single point of contact for common-area cleaning, multi-tenant restroom programs, and day porter coverage, without managing multiple vendor relationships across a portfolio.</p>
<p>We route service requests to insured, bonded local crews sized to the building, whether that is a single-story medical suite on Grand Avenue or a multi-story office building near Loop 101. Every crew works from a written scope of work agreed before the first clean, so tenants and ownership know exactly what is covered.</p>
<h2>What We Focus On</h2>
<p>Commercial buildings in the Peoria area deal with conditions a generic cleaning contract does not always account for: monsoon-season dust on entry glass, extreme summer heat that stresses HVAC intake grilles and accelerates exterior soiling, and a tenant mix that in places like Sun City and Sun City West skews toward medical offices serving an older-adult population. We scope service around the building, not a one-size template.</p>
<h2>How We Work</h2>
<p>Every engagement starts with a walkthrough of your property, not a phone-quoted number based on square footage alone. From there we put together a written scope of work covering exactly what's included, at what frequency, and what our response-time commitment is. That document becomes the reference point for both sides for the life of the engagement, which matters when a tenant complaint or a CAM reconciliation question comes up months later.</p>
<h2>Who We Work With</h2>
<p>Our clients are property managers overseeing single buildings or small portfolios, building engineers responsible for day-to-day facility condition, and REIT asset managers who need consistent, documented service across properties in this market without managing each vendor relationship individually. If that describes your role, our process is built around the accountability and documentation your position requires.</p>
<p>For a written quote or to discuss coverage for your property, use our <a href="/request-a-quote/">quote request form</a> or call {PHONE}.</p>
""",
)

core_page(
    "/contact/",
    f"Contact | Commercial Building Cleaning Peoria, AZ",
    f"Contact {BRAND} for commercial building cleaning in Peoria, AZ. Call {PHONE} or email {EMAIL}. Hours: {HOURS}.",
    f"Contact {BRAND}",
    f"""
<p>Reach out for a free quote, a question about coverage, or to discuss service for a property in your portfolio. We reply next business day.</p>
<h2>Contact Details</h2>
<ul>
<li><strong>Phone:</strong> <a href="tel:{PHONE_TEL}">{PHONE}</a></li>
<li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><strong>Hours:</strong> {HOURS}</li>
<li><strong>Service area:</strong> Peoria, AZ and surrounding West Valley communities within a 25-mile radius</li>
</ul>
<p>Because our office hours run {HOURS}, calls and emails received outside those hours get a callback the next business day. If you need a written quote, the fastest route is our <a href="/request-a-quote/">quote request form</a>.</p>
<h2>What to Have Ready</h2>
<p>If you're calling or emailing about a new property, having your building's approximate square footage, tenant count, and current cleaning arrangement (if any) ready speeds up the first conversation. If you're an existing client with a service issue, having the date and specific location of the issue helps us route it to the right crew immediately rather than spending the first exchange gathering details.</p>
<h2>Existing Clients</h2>
<p>If you're already working with us and have a same-day issue, such as a restroom supply shortage or a spill in a common area, call {PHONE} directly rather than using the form below, since the form is routed for new quote requests and general inquiries.</p>
<h2>Coordinating Across Multiple Properties</h2>
<p>If you manage more than one building in the Peoria area and want a single point of contact across your portfolio, mention that when you reach out. We can coordinate scheduling, reporting, and billing across multiple properties under one relationship rather than treating each building as a separate account with its own onboarding process and its own vendor contact.</p>
{quote_form_snippet('contact')}
""",
)

core_page(
    "/request-a-quote/",
    "Free Quote | Commercial Building Cleaning Peoria, AZ",
    f"Request a free commercial cleaning quote for your Peoria, AZ building. Insured crews, {YEARS} in the market. Next-business-day response.",
    "Request a Free Cleaning Quote in Peoria",
    f"""
<p>Tell us about your building and what needs covering, and we will follow up with a written quote. We reply next business day, every business day.</p>
<h2>What We Need From You</h2>
<ul>
<li>Approximate square footage and number of tenants</li>
<li>Which services you're evaluating: common area, restrooms, day porter, or a combination</li>
<li>Current cleaning frequency, if any, and where the gaps are</li>
</ul>
<h2>What Happens Next</h2>
<ol class="protocol-list">
<li>We review your request and, if useful, schedule a walkthrough of the property.</li>
<li>We put together a written scope of work matched to your building.</li>
<li>You get a quote with clear pricing, not a vague estimate.</li>
</ol>
<h2>Our Response-Time Commitment</h2>
<p>Our office hours are {HOURS}. Requests submitted during or outside those hours get a reply the next business day, in writing. We don't leave quote requests unanswered for a week while you wait to hear whether your building is even in our service area; if there's a coverage question, we'll tell you directly rather than letting the request go quiet.</p>
{quote_form_snippet('rfq')}
<p>A sample scope-of-work document is available on request once we've discussed your property. Prefer to talk it through first? Call {PHONE} during our {HOURS} business hours.</p>
<h2>Quoting a Portfolio of Buildings</h2>
<p>If you're requesting a quote for more than one property, note that in your submission. We scope each building individually since square footage, tenant mix, and traffic pattern vary by property, but we coordinate the quoting and onboarding process across your whole portfolio under one point of contact rather than treating each building as a separate transaction with its own back-and-forth and its own paperwork.</p>
""",
)

core_page(
    "/pricing/",
    "Commercial Building Cleaning Cost Peoria, AZ | Pricing Guide",
    f"Commercial building cleaning pricing in Peoria, AZ varies by square footage, tenant mix, and frequency. Request a written quote from {BRAND}.",
    "Commercial Building Cleaning Pricing in Peoria, AZ",
    f"""
<p>Commercial cleaning pricing depends on square footage, the number of tenants sharing common areas, service frequency, and the specific scope: common-area cleaning, restroom programs, day porter coverage, or a combination. Because building stock in the Peoria area ranges from single-story medical suites on Grand Avenue to multi-story office buildings near Loop 101, a flat per-square-foot rate rarely reflects what a specific property actually needs.</p>
<h2>What Drives Your Price</h2>
<ul>
<li><strong>Square footage and layout.</strong> A single-tenant standalone building scopes differently than a multi-tenant complex with shared corridors.</li>
<li><strong>Tenant mix.</strong> Medical and healthcare tenants typically require more frequent restroom service and touchpoint disinfection than a standard professional office.</li>
<li><strong>Frequency.</strong> Nightly, every-other-day, and weekly schedules price differently, and some buildings mix frequencies across services.</li>
<li><strong>Day porter coverage.</strong> On-site daytime staffing is quoted separately from after-hours cleaning.</li>
</ul>
<h2>Getting an Accurate Number</h2>
<p>Pricing varies by square footage, space type, and frequency. The most accurate way to get a number for your property is a written quote based on your building's actual scope. <a href="/request-a-quote/">Request a written quote</a> and we'll follow up with pricing matched to your property, not a generic range that doesn't reflect what you actually need.</p>
<h2>Why We Don't Publish a Flat Rate</h2>
<p>A single-tenant office building with one shared lobby costs less to service than a multi-tenant building at the same square footage with several shared restroom cores and higher common-area traffic. A per-square-foot number that ignores that difference either overcharges the simpler building or undercharges the more complex one, and neither outcome serves you. Instead, every quote is built from your building's actual layout and tenant mix.</p>
<h2>What to Have Ready When You Ask for a Quote</h2>
<p>To get an accurate number quickly, have your building's approximate square footage, tenant count, current restroom core count, and any known scheduling constraints ready. If you have an existing cleaning contract, having that scope on hand helps us identify gaps or overlaps rather than starting from zero.</p>
<p>See our <a href="/resources/building-cleaning-cost/">detailed guide to what drives cleaning costs in the Peoria market</a> for a deeper look at the variables, or <a href="/request-a-quote/">request a quote</a> now.</p>
""",
)

core_page(
    "/our-process/",
    f"Our Process & Guarantee | {BRAND} Peoria, AZ",
    f"How {BRAND} onboards a new commercial building in Peoria, AZ: walkthrough, written scope, crew assignment, first clean, 30-day check-in.",
    "What to Expect: Your First 30 Days in Peoria",
    f"""
<p>Bringing on a new commercial cleaning vendor is a decision that affects tenant experience, so we run a consistent process from first contact through the first month of service.</p>
<ol class="protocol-list">
<li><strong>Walkthrough.</strong> We assess your building's layout, tenant mix, and any specific conditions, such as a medical suite needing tighter restroom rotation or an entry that catches more dust after a windstorm.</li>
<li><strong>Written scope of work.</strong> Before any cleaning starts, you get a written scope covering exactly what's included, at what frequency, and what the response-time commitment is.</li>
<li><strong>Crew assignment.</strong> We assign an insured, bonded crew sized to your building rather than stretching a small team across too large a property.</li>
<li><strong>First clean.</strong> The first service visit gets extra attention to bring the building up to the agreed standard before settling into the regular rotation.</li>
<li><strong>30-day check-in.</strong> One month in, we check in on how service is going and adjust scope if your building's needs have shifted.</li>
</ol>
<h2>Response-Time Commitment</h2>
<p>Our office hours are {HOURS}. Requests and issues submitted outside those hours get a response the next business day, in writing, every time.</p>
<h2>Adjusting Scope as Your Building Changes</h2>
<p>Buildings change: a new tenant moves in, foot traffic shifts, a medical practice signs a lease and brings different sanitation expectations than the office tenant it replaced. The 30-day check-in is designed to catch that early, but scope isn't locked to a single annual review. If your building's needs shift mid-term, we adjust the written scope rather than letting service quietly drift out of sync with what the property actually requires.</p>
<h2>What We Don't Do</h2>
<p>We don't ask you to take our word for quality. Every scope of work includes specific, checkable language, not vague descriptions like "cleaned as needed." If you want to see what that looks like in practice, see our guide to <a href="/resources/common-area-standards/">common area cleaning standards that hold up to inspection</a>.</p>
""",
)

core_page(
    "/why-choose-us/",
    f"Why Choose {BRAND} | Peoria, AZ",
    f"Why Peoria, AZ property managers choose {BRAND}: {YEARS}, insured and bonded crews, transparent pricing, and a written scope on every job.",
    "Why Peoria Buildings Choose Us",
    f"""
<p>Property managers and building engineers in the Peoria area choose us for reasons that matter more to a commercial building than a five-star badge: a documented track record, insured crews, and pricing that's stated plainly rather than negotiated in the dark.</p>
<h2>What Sets Us Apart</h2>
<ul>
<li><strong>{YEARS} in the Peoria market.</strong> We've worked buildings through monsoon seasons, extreme summer heat, and the tenant turnover that comes with a growing West Valley economy.</li>
<li><strong>Insured and bonded.</strong> Every job runs under coverage appropriate for commercial cleaning operations, with a certificate of insurance included on every written quote.</li>
<li><strong>Written scope of work.</strong> No verbal promises. What's covered, how often, and what it costs is documented before the first clean.</li>
<li><strong>Transparent pricing.</strong> We quote based on your building's actual scope rather than a generic per-square-foot number that doesn't reflect your tenant mix.</li>
<li><strong>Response-time commitment.</strong> Requests get a next-business-day reply, every time, during our {HOURS} hours.</li>
</ul>
<p>Most incumbent cleaning contractors in this market don't publish pricing, don't put scope in writing, and don't commit to a response time. We do all three.</p>
<h2>No Fabricated Trust Signals</h2>
<p>We don't publish testimonials, star ratings, or review counts. Those are easy to fabricate and hard for a prospective client to verify, and the FTC's Consumer Review Rule has made fabricated reviews a real liability for any business that publishes them, whether generated in-house or purchased. Instead, our credibility rests on documentation you can check yourself: our insurance status, our written process, and a direct conversation about your building's specific needs.</p>
<h2>A Track Record Built on the Buildings We Service</h2>
<p>Most incumbents in this market compete on a five-star badge. We'd rather compete on a written scope of work you can hold us to, a response time we commit to in writing, and {YEARS} of experience with the specific conditions this market presents, from monsoon-season entry care to the tenant mix differences between a downtown office tower and a Sun City medical suite.</p>
""",
)

core_page(
    "/faq/",
    "Commercial Building Cleaning FAQ | Peoria, AZ",
    f"Answers to common questions about commercial building cleaning in Peoria, AZ: pricing, scheduling, insurance, and service area.",
    "Commercial Building Cleaning FAQs for Peoria Businesses",
    f"""
<div class="faq-item">
<h3>What areas do you serve?</h3>
<p>We serve commercial buildings within a 25-mile radius of Peoria, Arizona, including Glendale, Sun City, Surprise, El Mirage, Youngtown, Waddell, Sun City West, and parts of Phoenix. See our <a href="/service-areas/">full service area list</a>.</p>
</div>
<div class="faq-item">
<h3>How much does commercial cleaning cost?</h3>
<p>Pricing depends on square footage, tenant mix, and frequency. We don't publish a flat rate because it wouldn't reflect what your building actually needs. See our <a href="/pricing/">pricing page</a> or request a written quote.</p>
</div>
<div class="faq-item">
<h3>Are your crews insured?</h3>
<p>Yes. We carry general liability insurance appropriate for commercial cleaning operations, and a certificate of insurance is included with every written quote. Details are on our <a href="/insured-and-bonded/">insured and bonded page</a>.</p>
</div>
<div class="faq-item">
<h3>What's the difference between day porter service and standard cleaning?</h3>
<p>Day porter service is on-site coverage during business hours, handling spills, restocking, and common-area upkeep as issues come up. Standard common-area and restroom cleaning happens on a scheduled after-hours or set-frequency basis. See our <a href="/services/day-porter-services/">day porter services page</a>.</p>
</div>
<div class="faq-item">
<h3>How quickly do you respond to requests?</h3>
<p>Our hours are {HOURS}. Requests submitted during or outside those hours get a response the next business day.</p>
</div>
<div class="faq-item">
<h3>Do you serve medical office buildings?</h3>
<p>Yes. We work with medical and healthcare tenants across the service area, including the medical office clusters in Sun City and Sun City West, and scope restroom and common-area service accordingly.</p>
</div>
<div class="faq-item">
<h3>Can I combine services into one scope of work?</h3>
<p>Yes. Most buildings combine common-area cleaning with a restroom program, and larger or higher-traffic buildings often add day porter coverage. We build one written scope covering everything you need rather than managing separate contracts for each service.</p>
</div>
<div class="faq-item">
<h3>What happens if I'm not satisfied with a specific visit?</h3>
<p>Contact us directly with the date and location of the issue. We log every complaint and route it back to the crew, with same-day response for anything involving sanitation or safety. See our <a href="/resources/tenant-complaint-playbook/">tenant complaint playbook</a> for how we recommend property managers track and escalate issues.</p>
</div>
<div class="faq-item">
<h3>Do you provide a written scope of work before service starts?</h3>
<p>Always. Every engagement starts with a written scope covering exactly what's included, at what frequency, and what our response-time commitment is. Nothing runs on a verbal agreement.</p>
</div>
<div class="faq-item">
<h3>How does seasonal weather affect service?</h3>
<p>Monsoon season, roughly mid-June through September, brings dust storms that can leave visible film on entry glass and lobby flooring within hours. Buildings closer to open desert, such as those in Waddell or Sun City West, tend to need more frequent entry-glass attention during this stretch. We scope seasonal variation into the schedule rather than treating it as a surprise add-on.</p>
</div>
""",
)

core_page(
    "/insured-and-bonded/",
    "Insured & Bonded Commercial Building Cleaning | Peoria, AZ",
    f"{BRAND} crews are insured and bonded, with {YEARS} serving Peoria, AZ commercial buildings. Certificate of insurance included with every quote.",
    f"Insured, Bonded and {YEARS} Serving Peoria",
    f"""
<p>Commercial buildings carry liability exposure that a homeowner's cleaning arrangement doesn't, which is why every crew we coordinate work through carries general liability insurance appropriate for commercial cleaning operations. A certificate of insurance is included with every written quote, so your property management company or ownership group has documentation on file before service starts.</p>
<h2>Bonding</h2>
<p>Crews working in your building's common areas and shared spaces are bonded, providing an added layer of protection appropriate for multi-tenant commercial properties.</p>
<h2>{YEARS} in the Peoria Market</h2>
<p>{BRAND} has coordinated commercial cleaning coverage across Peoria and the surrounding West Valley for {YEARS}. That track record means we've built relationships with crews who understand what a multi-tenant office building, a medical suite, or a light-industrial property actually needs, rather than applying a residential-cleaning mindset to a commercial contract.</p>
<h2>Documentation for Your Property File</h2>
<p>If your property management company requires a certificate of insurance on file before granting building access, request one along with your written quote and we'll include it as part of onboarding.</p>
<h2>Why This Matters More in a Multi-Tenant Building</h2>
<p>A cleaning crew working in a multi-tenant building's shared spaces carries different liability exposure than one working in a single-tenant suite. Shared lobbies, elevator interiors, and restroom cores see traffic from every tenant in the building, not just one, which means insurance coverage appropriate for that exposure matters more, not less, than it would for a standalone office. We treat that distinction as part of how we scope every multi-tenant engagement.</p>
<h2>What We Don't Publish</h2>
<p>We don't publish specific policy numbers or dollar coverage amounts on this page, and we won't invent figures to fill space. If your property file requires those specifics, they're provided directly with your certificate of insurance rather than posted publicly where they serve no purpose beyond appearing complete.</p>
<p>Questions about coverage before requesting a quote? Call {PHONE} or see our <a href="/our-process/">process page</a> for how insurance documentation fits into onboarding.</p>
""",
)

# ---------------------------------------------------------------------------
# SERVICES HUB
# ---------------------------------------------------------------------------
services_hub_body = """
<p>We coordinate three core service lines for commercial buildings across the Peoria, Arizona area. Each can run standalone or combined into a single scope of work for your property.</p>
<div class="card-grid">
"""
service_hub_descs = {
    "common-area-lobby-cleaning": "Lobby floors, entry glass, elevator interiors, stairwells, and shared corridors serviced on a schedule tenants notice.",
    "multi-tenant-restroom-programs": "Scheduled restocking, disinfection, and fixture checks across shared restroom cores in multi-tenant buildings.",
    "day-porter-services": "On-site daytime staffing for spills, restocking, and common-area upkeep during business hours.",
}
for slug, name in SERVICES:
    services_hub_body += f"""  <div class="card">
    <h3>{name}</h3>
    <p>{service_hub_descs[slug]}</p>
    <a class="card-link" href="/services/{slug}/">Learn more &rarr;</a>
  </div>
"""
services_hub_body += f"""</div>

<h2>Combining Services</h2>
<p>Most buildings don't need just one of these services in isolation. A common structure pairs common-area cleaning with a restroom program under one scope of work, and larger or higher-traffic buildings add day porter coverage to close the gap between scheduled visits. We build one written scope covering whatever combination fits your property rather than requiring separate contracts per service.</p>

<h2>How We Scope Service to Your Building</h2>
<p>Every engagement starts with a walkthrough, not a phone-quoted estimate. We look at your building's layout, tenant mix, and traffic pattern, then put together a written scope specific to what you actually need. A single-story medical suite in Sun City gets scoped differently than a multi-story office building near Loop 101, because the traffic pattern, restroom core count, and seasonal exposure are genuinely different.</p>

<h2>Insured and Documented</h2>
<p>Every service line runs under insurance coverage appropriate for commercial cleaning operations, with a certificate of insurance included on every written quote. See our <a href="/insured-and-bonded/">insured and bonded page</a> for details, or our <a href="/our-process/">process page</a> for how a new engagement moves from walkthrough to first clean.</p>

<p>Not sure which combination fits your building? <a href="/request-a-quote/">Request a quote</a> and we'll help you scope it, or browse services by <a href="/service-areas/">service area</a>.</p>
"""
core_page(
    "/services/",
    "Commercial Building Cleaning Services | Peoria, AZ",
    "Common area cleaning, multi-tenant restroom programs, and day porter services for commercial buildings in Peoria, AZ.",
    "Our Commercial Building Cleaning Services in Peoria",
    services_hub_body,
)

print(f"Built {len(pages_built)} pages so far: home + 8 core + services hub")

# ---------------------------------------------------------------------------
# Delegate remaining page groups to sibling modules (services, areas, resources)
# ---------------------------------------------------------------------------
import generate_services
import generate_areas
import generate_resources

pages_built.extend(generate_services.build(core_page))
pages_built.extend(generate_areas.build())
pages_built.extend(generate_resources.build(core_page))

print(f"TOTAL PAGES BUILT: {len(pages_built)}")

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_pages_built.txt"), "w") as f:
        f.write("\n".join(sorted(pages_built)))
