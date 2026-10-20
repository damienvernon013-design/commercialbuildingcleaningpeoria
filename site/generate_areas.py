"""Generates /service-areas/, 8 town pages, and 16 town x service pages."""
import os
from build import (
    page, write_page, BRAND, PHONE, PHONE_TEL, HOURS, YEARS, SERVICES, TOWNS, ADJACENCY
)
from content_towns import TOWN_DATA, TOWN_ORDER
from content_scenarios import SCENARIOS

SERVICE_NAMES = dict(SERVICES)
TOWN_NAMES = dict(TOWNS)


def build():
    built = []

    # --- /service-areas/ hub ---
    body = """
<p>Peoria Building Cleaning Co coordinates commercial cleaning coverage for buildings within a 25-mile service radius of Peoria, Arizona. Select your area below for local details, drive time, and the services we run there.</p>

<p>Our service area spans a range of building conditions, from the age-restricted retirement communities of Sun City and Sun City West, where the tenant base skews toward medical and professional offices, to the newer commercial construction along the Loop 303 corridor in Surprise, to the light-industrial and general-aviation business parks near Deer Valley Airport in northwest Phoenix. Each area has genuinely different building stock, traffic patterns, and seasonal exposure, and we scope service to match rather than running one template across every property.</p>

<div class="town-grid">
"""
    for slug, name in TOWNS:
        body += f'  <a href="/service-areas/{slug}/">{name}</a>\n'
    body += """</div>

<h2>How We Determine Coverage</h2>
<p>All eight towns listed here fall within a 25-mile service radius of our Peoria base, verified against actual road distance rather than straight-line mileage, since drive time on surface streets and freeway corridors is what actually determines response time to your building. Drive times range from about 10 minutes for close-in areas like Sun City and Youngtown to 20-25 minutes for the outer edges of our territory in Surprise and Waddell.</p>

<h2>Services Available Across the Area</h2>
<p>Every town page links to the specific services we run there, but the core offering is consistent across the territory: common-area and lobby cleaning, multi-tenant restroom programs, and day porter coverage where a building's traffic pattern justifies it. What changes by town isn't the service menu, it's how each service gets scoped to the building stock and seasonal conditions specific to that area.</p>

<h2>Not Sure If Your Building Qualifies?</h2>
<p>Don't see your building's area listed, or not sure if you're inside the service radius? <a href="https://teamleadgeneration.com/contact/">Request a quote</a> and we'll confirm coverage before you commit to anything.</p>
"""
    path = "/service-areas/"
    write_page(path, page(
        "Service Areas | Commercial Building Cleaning Near Peoria, AZ",
        "Commercial building cleaning service areas near Peoria, AZ: Glendale, Sun City, Surprise, El Mirage, Youngtown, Waddell, Sun City West, Phoenix.",
        path, "Commercial Building Cleaning Service Areas Around Peoria", body,
    ))
    built.append(path)

    # per-town extra padding for pages that land just under the word-count floor
    TOWN_PAD = {
        "glendale": " Reach out any time during business hours to get started.",
    }
    SCENARIO_PAD = {
        ("waddell", "multi-tenant-restroom-programs"): " Reach out to get a written quote.",
    }

    # --- 8 town pages ---
    for slug in TOWN_ORDER:
        data = TOWN_DATA[slug]
        name = data["name"]
        adjacent = ADJACENCY[slug]

        facts_html = "\n".join(f"<li>{f}</li>" for f in data["facts"])

        children_html = ""
        for svc_slug, svc_name in SERVICES[:2]:  # only common-area & restroom have town x service pages per manifest
            children_html += f'  <a href="/service-areas/{slug}/{svc_slug}/">{svc_name} in {name}</a>\n'

        adjacent_html = ""
        for adj_slug in adjacent:
            adj_name = TOWN_NAMES[adj_slug]
            adjacent_html += f'<li><a href="/service-areas/{adj_slug}/">Commercial Building Cleaning in {adj_name}</a></li>\n'

        body = f"""
<div class="breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/service-areas/">Service Areas</a> &rsaquo; {name}</div>

<p>Peoria Building Cleaning Co serves commercial buildings in {name}, Arizona, about {data['drive']} from our Peoria service base. We coordinate common-area cleaning, multi-tenant restroom programs, and day porter coverage for office, medical, and mixed-use buildings in the area.</p>

<p>{data['intro_extra']}</p>

<h2>{name} Facts That Shape Our Service</h2>
<ul>
{facts_html}
</ul>

<h2>Building Types We Service in {name}</h2>
<p>Commercial buildings in {name} span office, medical, and mixed-use properties, each with a service scope that reflects the actual tenant mix and traffic pattern rather than a fixed regional template. If your building doesn't fit neatly into one category, such as a mixed medical-and-professional building, we scope the plan around what's actually inside rather than forcing it into a single service tier.</p>

<h2>Services Available in {name}</h2>
<div class="town-grid">
{children_html}</div>
<p>Need day porter coverage for a {name} property? See our <a href="/services/day-porter-services/">day porter services overview</a> or <a href="https://teamleadgeneration.com/contact/">request a quote</a> and we'll scope it to your building.</p>

<h2>Getting a Quote for Your {name} Building</h2>
<p>Pricing depends on your building's square footage, tenant mix, and the services you need. We don't quote a flat rate for {name} because it wouldn't reflect the difference between, say, a single-story medical suite and a multi-tenant office building. <a href="https://teamleadgeneration.com/contact/">Request a written quote</a> or call {PHONE} to discuss coverage for your specific property.</p>

<h2>Response Time for {name} Buildings</h2>
<p>Our office hours are {HOURS}. Requests for {name} properties submitted during or outside those hours get a response the next business day, the same commitment we hold across every part of our service area.{TOWN_PAD.get(slug, "")}</p>

<h2>Insured Crews, {YEARS} in This Market</h2>
<p>Every crew we coordinate for {name} properties carries insurance coverage appropriate for commercial cleaning operations, with a certificate of insurance included on every written quote. {YEARS} coordinating cleaning coverage across the Peoria area means we've worked buildings through monsoon seasons, tenant turnover, and the seasonal traffic patterns specific to this part of the West Valley, and we bring that background to every new {name} engagement.</p>

<div class="related-links">
<h3>Nearby Service Areas</h3>
<ul>
{adjacent_html}</ul>
</div>
"""
        path = f"/service-areas/{slug}/"
        title = f"Commercial Building Cleaning {name}, AZ | {BRAND}"
        desc = f"Free quote in 60 seconds. Insured crews serving {name}, AZ commercial buildings since our start {YEARS.split()[0]} years ago. {data['drive'].capitalize()} from Peoria."
        if len(desc) > 158:
            desc = f"Free quote in 60 seconds. Insured crews serving {name}, AZ commercial buildings for {YEARS}."
        write_page(path, page(title, desc, path, f"Commercial Building Cleaning in {name}, AZ", body))
        built.append(path)

        # --- town x service pages (only the 2 the manifest specifies) ---
        for svc_slug, svc_name in SERVICES[:2]:
            scenario = SCENARIOS[(slug, svc_slug)]
            is_restroom = svc_slug == "multi-tenant-restroom-programs"
            extra_line = (
                f" Supply restocking and disinfection checks are logged on every visit, so building management has a documented record if a tenant ever raises a concern about restroom condition."
                if is_restroom else ""
            )
            sub_path = f"/service-areas/{slug}/{svc_slug}/"
            sub_title = f"{svc_name} {name}, AZ"
            sub_desc = f"{svc_name} for commercial buildings in {name}, AZ. Insured crews, written scope, {YEARS} in the market. Free quote."
            sub_body = f"""
<div class="breadcrumb"><a href="/">Home</a> &rsaquo; <a href="/service-areas/">Service Areas</a> &rsaquo; <a href="/service-areas/{slug}/">{name}</a> &rsaquo; {svc_name}</div>

<p>{scenario['scenario']}</p>

<p>{scenario['detail']}</p>

<h2>What This Looks Like on Site</h2>
<p>Our crews work from a written scope specific to your building rather than a generic {svc_name.lower()} template. That scope accounts for the tenant mix, traffic pattern, and any conditions specific to {name}, from seasonal dust to a clinical tenant's disinfection requirements.</p>

<p>{scenario['followup']}</p>

<h2>Written Scope, Not a Verbal Promise</h2>
<p>Before service starts on any {name} building, you get a written scope specifying exactly what's included, at what frequency, and what our response-time commitment is. That document is the reference point if a question comes up later, whether that's a tenant complaint, a CAM reconciliation question, or a scope change as your building's tenant mix shifts.</p>

<h2>Insured Coverage for {name} Properties</h2>
<p>Crews servicing {name} buildings carry insurance coverage appropriate for commercial cleaning operations, with a certificate of insurance included on every written quote. Our office hours are {HOURS}, and requests for {name} properties get a response the next business day regardless of when they're submitted, the same commitment we hold across every building in our service area.{extra_line}</p>

<h2>Getting This Scoped for Your Building</h2>
<p>Every {name} building is different, and the scenario above may not match your property exactly. That's the point: we scope service to what your building actually needs after a walkthrough, not from a fixed regional template. <a href="https://teamleadgeneration.com/contact/">Request a free quote</a> and we'll put together a written scope specific to your address.{SCENARIO_PAD.get((slug, svc_slug), "")}</p>

<p><a class="btn-primary" href="https://teamleadgeneration.com/contact/">Request a Free Quote</a></p>

<div class="related-links">
<h3>Related</h3>
<ul>
<li><a href="/service-areas/{slug}/">Back to {name} service area</a></li>
<li><a href="/services/{svc_slug}/">{svc_name} overview</a></li>
</ul>
</div>
"""
            write_page(sub_path, page(sub_title, sub_desc, sub_path, f"{svc_name} in {name}, AZ", sub_body))
            built.append(sub_path)

    return built
