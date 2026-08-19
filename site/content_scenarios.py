"""Concrete building scenarios for each town x service combination (16 pages).
Each scenario is specific enough it could not be find-and-replaced across towns."""

# key: (town_slug, service_slug) -> scenario paragraph + details
SCENARIOS = {
    ("glendale", "common-area-lobby-cleaning"): {
        "scenario": "A three-story professional office building near the Westgate Entertainment District leases suites to a mix of insurance agents, a physical therapy practice, and a regional bank branch. The ground-floor lobby and elevator lobbies see a spike in foot traffic on Cardinals home game days and concert nights at Desert Diamond Arena, when nearby parking overflow sends extra pedestrian traffic past the building's entrance.",
        "detail": "Event-day surges mean lobby glass, entry mats, and elevator interiors need a second pass beyond the standard nightly service, timed around the venue schedule rather than a fixed weekly rotation.",
    
        "followup": "Our crews time the extra event-day pass to the Cardinals and Coyotes-adjacent event calendar rather than a fixed day of the week, so the second visit actually lines up with when foot traffic spikes rather than an arbitrary schedule.",
    },
    ("glendale", "multi-tenant-restroom-programs"): {
        "scenario": "A two-story medical and professional building off 75th Avenue near Arrowhead Towne Center houses a dental practice, an urgent care clinic, and several small offices sharing two common restroom cores per floor.",
        "detail": "With a healthcare tenant on-site, restroom supply levels and touchpoint disinfection get checked and logged on every visit, not just restocked when empty.",
    
        "followup": "Because the building's tenant mix includes an urgent care clinic, restroom service here runs on a daily rather than every-other-day rotation, with disinfection logs kept for the clinic's own compliance records if requested.",
    },
    ("sun-city", "common-area-lobby-cleaning"): {
        "scenario": "A single-story medical office building on Grand Avenue houses three physician practices sharing a central lobby and waiting area. Given the age-restricted resident population, the entrance and lobby floor need slip-resistant care and mobility-aid-friendly clearance, not just a clean shine.",
        "detail": "Nightly service focuses on low-glare floor finish and clear, obstruction-free walkways rather than the high-traffic churn a downtown office tower would need.",
    
        "followup": "We use floor products rated for slip resistance rather than a high-gloss finish that looks impressive but creates a hazard for a mobility-aid-dependent patient population moving between three physician practices.",
    },
    ("sun-city", "multi-tenant-restroom-programs"): {
        "scenario": "A single-story professional building near 99th Avenue houses a bank branch, an insurance office, and a small medical practice sharing one set of ADA-compliant restrooms.",
        "detail": "Grab bars, non-slip flooring, and accessible fixture heights get checked as part of every restroom service visit, matching the building's older-adult tenant base.",
    
        "followup": "Fixture checks here include verifying grab bars haven't loosened and that accessible stall clearance hasn't been blocked by supply storage, issues that matter more in a building serving this population than in a standard office restroom.",
    },
    ("surprise", "common-area-lobby-cleaning"): {
        "scenario": "A two-story office building in the Prasada development near Bell Road and Loop 303 leases to a mortgage brokerage, a staffing agency, and a telehealth practice sharing a shared lobby and stairwell.",
        "detail": "Newer construction means glass entry doors and polished concrete common areas that show dust quickly during Surprise's more open desert exposure, so entryway glass gets attention on every visit, not just weekly.",
    
        "followup": "The polished concrete common areas typical of this newer construction show streaking differently than older tile or carpet, so our crews use a glass and hard-floor protocol suited to the surface rather than a generic all-purpose approach.",
    },
    ("surprise", "multi-tenant-restroom-programs"): {
        "scenario": "A retail-office building near the Surprise Recreation Campus sees seasonal spikes in foot traffic each spring during stadium events, straining shared restroom supplies faster than the rest of the year.",
        "detail": "Supply levels get checked more frequently during spring training season and scaled back to standard rotation the rest of the year, rather than running one fixed schedule year-round.",
    
        "followup": "We coordinate the seasonal ramp-up directly with the building manager each spring rather than waiting for a supply-shortage complaint to trigger the schedule change.",
    },
    ("el-mirage", "common-area-lobby-cleaning"): {
        "scenario": "A single-story professional building on an irregular lot along Grand Avenue houses a small law office, a tax preparation firm, and a check-cashing business sharing one shared entry and small lobby.",
        "detail": "The angled Grand Avenue frontage means the entry walkway collects more windblown dust than a standard rectangular-lot building, so exterior entry sweeping is built into the standard visit rather than treated as an add-on.",
    
        "followup": "The entry sweep here is scheduled every visit rather than as a periodic add-on, since the angled lot means dust accumulates faster than a standard rectangular frontage would see.",
    },
    ("el-mirage", "multi-tenant-restroom-programs"): {
        "scenario": "A small professional building near the municipal campus area houses two offices sharing a single restroom core, with modest daily traffic compared to larger commercial nodes nearby.",
        "detail": "Lower daily traffic means the restroom program runs on a leaner supply-check schedule, sized to the building rather than a one-size program built for a larger complex.",
    
        "followup": "A leaner schedule here means lower cost for the building without sacrificing the supply-check documentation that protects the property manager if a tenant does raise a concern.",
    },
    ("youngtown", "common-area-lobby-cleaning"): {
        "scenario": "A small retail-office strip on 111th Avenue houses a real estate office, a barber shop, and an accounting firm sharing a common walkway rather than an enclosed lobby.",
        "detail": "Because the common area is an open-air walkway rather than a climate-controlled lobby, service focuses on entry glass, walkway sweeping, and trash management rather than interior floor care.",
    
        "followup": "Because there's no enclosed lobby to climate-control, our focus shifts to entry glass and walkway sweeping rather than interior floor finish, which keeps the scope, and the cost, aligned with what this building type actually needs.",
    },
    ("youngtown", "multi-tenant-restroom-programs"): {
        "scenario": "A compact professional building near Grand Avenue houses two small tenants sharing a single restroom, typical of Youngtown's limited commercial inventory.",
        "detail": "The restroom program here is scaled to a two-tenant building, checked on a lighter rotation than a larger multi-tenant complex would need.",
    
        "followup": "This is a straightforward, low-cost program for a two-tenant building, without the padded scope a larger multi-service contract would carry.",
    },
    ("waddell", "common-area-lobby-cleaning"): {
        "scenario": "A standalone single-story office building near Cotton Lane serves an agricultural equipment dealer's administrative offices, with a small public-facing lobby adjacent to White Tank Mountain Regional Park.",
        "detail": "Proximity to open desert means entry glass and lobby flooring collect more windblown dust after storms than buildings closer to the urban core, so post-wind-event cleaning gets scheduled reactively in addition to the standard rotation.",
    
        "followup": "Rather than a fixed weekly-only schedule, we build in a reactive visit after any significant wind event, since a single haboob can undo a week of standard upkeep at this property's exposure level.",
    },
    ("waddell", "multi-tenant-restroom-programs"): {
        "scenario": "A small commercial building near the Cotton Lane corridor houses two tenants sharing a single restroom facility, reflecting the area's lower commercial density.",
        "detail": "Service is scoped to a single restroom core with straightforward supply management rather than a multi-core program.",
    
        "followup": "With only one restroom core to manage, this runs as a simple, predictable program without the complexity a multi-core building would require.",
    },
    ("sun-city-west", "common-area-lobby-cleaning"): {
        "scenario": "A medical office building on R.H. Johnson Boulevard houses an ophthalmology practice, a physical therapy clinic, and a hearing aid center sharing a central lobby with mobility-aid-friendly entry.",
        "detail": "The lobby's proximity to open desert toward Hassayampa means end-of-day dust accumulation on entry glass is more consistent here, so glass and entry-mat service are built into every visit rather than a weekly add-on.",
    
        "followup": "Given the practice mix, mobility-aid clearance and non-slip flooring are treated as core requirements here, not an accommodation added after the fact.",
    },
    ("sun-city-west", "multi-tenant-restroom-programs"): {
        "scenario": "A single-story medical building near R.H. Johnson Boulevard shares restroom facilities across three physician suites serving a predominantly older-adult patient base.",
        "detail": "ADA fixture checks, grab-bar security, and non-slip flooring maintenance are part of every restroom visit, matching the clinical and age-restricted context of the building.",
    
        "followup": "Because three physician suites share this restroom core, supply consumption runs higher than a standard office building at similar square footage, and the check frequency reflects that.",
    },
    ("phoenix", "common-area-lobby-cleaning"): {
        "scenario": "A two-story light-industrial and office building near Deer Valley Airport off I-17 leases to an aviation parts distributor and two administrative office tenants sharing a shared lobby and stairwell.",
        "detail": "Light-industrial tenants track more grit and debris through the shared entry than a pure office building would, so entry mats and lobby floor care are scoped heavier here than at a standalone office property.",
    
        "followup": "We scope entry-mat replacement and lobby floor care around the debris pattern industrial tenants generate, which is a different maintenance profile than the office-only buildings elsewhere in our service area.",
    },
    ("phoenix", "multi-tenant-restroom-programs"): {
        "scenario": "A mixed-use building near the Metrocenter redevelopment area along I-17 houses several newly leased office suites sharing a restroom core still being brought up to current tenant standards.",
        "detail": "As redevelopment brings in new tenants, restroom supply levels and fixture condition get reassessed on a rolling basis rather than assuming the building's older baseline still applies.",
    
        "followup": "As new tenants lease into the redeveloped space, we reassess fixture condition and supply needs rather than assuming a static baseline that no longer reflects who's actually using the building.",
    },
}
