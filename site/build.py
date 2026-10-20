#!/usr/bin/env python3
"""Static site generator for commercialbuildingcleaningpeoria.com.
Reads page content from content.py and renders full HTML files."""
import os
import html

DOMAIN = "commercialbuildingcleaningpeoria.com"
BASE_URL = f"https://{DOMAIN}"
BRAND = "Peoria Building Cleaning Co"
PHONE = "(866) 958-8773"
PHONE_TEL = "+18669588773"
EMAIL = "ops@thequotemasters.com"
HOURS = "Mon–Fri 8:30am–5:00pm"
YEARS = "22 years"

SERVICES = [
    ("common-area-lobby-cleaning", "Common Area & Lobby Cleaning"),
    ("multi-tenant-restroom-programs", "Multi-Tenant Restroom Programs"),
    ("day-porter-services", "Day Porter Services"),
]

TOWNS = [
    ("glendale", "Glendale"),
    ("sun-city", "Sun City"),
    ("surprise", "Surprise"),
    ("el-mirage", "El Mirage"),
    ("youngtown", "Youngtown"),
    ("waddell", "Waddell"),
    ("sun-city-west", "Sun City West"),
    ("phoenix", "Phoenix"),
]

# Adjacency map: at most 2 geographically adjacent towns per town (never all siblings)
ADJACENCY = {
    "glendale": ["youngtown", "phoenix"],
    "sun-city": ["youngtown", "sun-city-west"],
    "surprise": ["el-mirage", "waddell"],
    "el-mirage": ["surprise", "youngtown"],
    "youngtown": ["sun-city", "el-mirage"],
    "waddell": ["surprise", "sun-city-west"],
    "sun-city-west": ["sun-city", "waddell"],
    "phoenix": ["glendale", "sun-city"],
}

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def slugify_town(name):
    return name.lower().replace(" ", "-")


def head(title, description, canonical_path, schema_extra=None):
    canonical = f"{BASE_URL}{canonical_path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="/styles.css">
</head>
"""


def local_business_schema():
    towns_json = ", ".join(f'"{name}"' for _, name in TOWNS)
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "email": "{EMAIL}",
  "url": "{BASE_URL}/",
  "areaServed": [{towns_json}, "Peoria"],
  "openingHours": "Mo-Fr 08:30-17:00",
  "priceRange": "$$"
}}
</script>
"""


def header_nav():
    return f"""<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="header-strapline">{YEARS} serving Peoria-area commercial buildings &middot; Insured &amp; bonded &middot; Response within one business day</div>
  <div class="container header-main">
    <div class="brand"><a href="/">{BRAND}</a></div>
    <div class="header-phone"><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
    <a class="header-cta" href="https://teamleadgeneration.com/contact/">Request a Free Quote</a>
  </div>
  <nav class="primary-nav" aria-label="Main navigation">
    <div class="container">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/services/">Services</a></li>
        <li><a href="/service-areas/">Service Areas</a></li>
        <li><a href="/pricing/">Pricing</a></li>
        <li><a href="/our-process/">Our Process</a></li>
        <li><a href="/why-choose-us/">Why Choose Us</a></li>
        <li><a href="/insured-and-bonded/">Insured &amp; Bonded</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
  </nav>
</header>
"""


def footer():
    town_links = "\n".join(
        f'<li><a href="/service-areas/{slug}/">{name}</a></li>'
        for slug, name in TOWNS
    )
    service_links = "\n".join(
        f'<li><a href="/services/{slug}/">{name}</a></li>'
        for slug, name in SERVICES
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>{BRAND}</h4>
        <p>Commercial building cleaning serving Peoria and the surrounding West Valley. {YEARS} in business. Insured and bonded.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          {service_links}
        </ul>
      </div>
      <div>
        <h4>Service Areas</h4>
        <ul>
          {town_links}
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{HOURS}</li>
          <li><a href="https://teamleadgeneration.com/contact/">Request a Quote</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-strapline">
      {YEARS} serving commercial buildings in the Peoria, AZ area. Insured and bonded. Serving Peoria and surrounding West Valley communities within a 25-mile service radius.
    </div>
  </div>
</footer>
"""


def quote_form_snippet(context_label="quote"):
    return f"""<div class="quote-form-wrap">
  <h2>Request a Free Quote</h2>
  <form class="quote-form" id="quote-form-{context_label}" data-lead-form>
    <div class="form-status" data-form-status role="status" aria-live="polite" hidden></div>
    <label for="first-name-{context_label}">First Name</label>
    <input type="text" id="first-name-{context_label}" name="first_name" required>
    <label for="last-name-{context_label}">Last Name</label>
    <input type="text" id="last-name-{context_label}" name="last_name" required>
    <label for="company-{context_label}">Company / Property Name</label>
    <input type="text" id="company-{context_label}" name="company_name">
    <label for="email-{context_label}">Email</label>
    <input type="email" id="email-{context_label}" name="email" required>
    <label for="phone-{context_label}">Phone</label>
    <input type="tel" id="phone-{context_label}" name="phone" required>
    <label for="zip-{context_label}">Building ZIP Code</label>
    <input type="text" id="zip-{context_label}" name="zip" inputmode="numeric" pattern="[0-9]{{5}}" maxlength="5" required>
    <label for="sqft-{context_label}">Approximate Square Footage</label>
    <input type="text" id="sqft-{context_label}" name="sqft">
    <label for="notes-{context_label}">What do you need cleaned?</label>
    <textarea id="notes-{context_label}" name="notes"></textarea>
    <button type="submit" class="btn-primary">Request My Quote</button>
  </form>
  <p class="form-note">We reply next business day. Hours: {HOURS}. Call {PHONE} or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
"""


def page(title, description, canonical_path, h1, body_html, breadcrumb_html="", extra_schema=""):
    doc = head(title, description, canonical_path)
    doc += "<body>\n"
    doc += local_business_schema()
    if extra_schema:
        doc += extra_schema
    doc += header_nav()
    doc += f'<main id="main">\n<div class="container">\n{breadcrumb_html}<h1>{h1}</h1>\n{body_html}\n</div>\n</main>\n'
    doc += footer()
    doc += '<script src="/lead-form.js" defer></script>\n'
    doc += "</body>\n</html>\n"
    return doc


def write_page(path, content):
    full_dir = os.path.join(OUT_DIR, path.strip("/"))
    os.makedirs(full_dir, exist_ok=True)
    with open(os.path.join(full_dir, "index.html"), "w") as f:
        f.write(content)


if __name__ == "__main__":
    print("build.py loaded as module; run generate_site.py to render pages")
