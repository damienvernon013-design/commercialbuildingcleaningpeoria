"""Per-town facts, drive times, and scenario data. Sourced from general West Valley
geographic knowledge; drive times are approximate planning estimates from Peoria, AZ."""

TOWN_DATA = {
    "glendale": {
        "name": "Glendale",
        "drive": "about 10-15 minutes (roughly 8-12 miles) north on Loop 101 or south on 67th Avenue",
        "facts": [
            "Glendale is home to the Westgate Entertainment District, adjacent to State Farm Stadium and Desert Diamond Arena, where multi-tenant office and retail buildings see heavy foot traffic on event days.",
            "The Arrowhead Towne Center corridor along 75th Avenue carries a dense mix of retail and professional office space that needs early-morning turnarounds before doors open.",
            "Loop 101 (the Agua Fria Freeway) forms Glendale's commercial spine and is the same corridor our crews use to reach the city, which keeps response times predictable.",
        ],
        "adjacent_note": "Glendale sits along the same Loop 101 corridor Peoria uses, and shares a border with north Phoenix office districts.",
        "intro_extra": "Glendale's building stock splits between the entertainment-district properties near Westgate, which see sharp traffic spikes tied to event schedules, and the steadier retail-office mix along Arrowhead Towne Center. A cleaning schedule that treats both the same way misses the point: one needs event-day flexibility, the other needs consistent daily service.",
    },
    "sun-city": {
        "name": "Sun City",
        "drive": "about 10 minutes (roughly 6-9 miles) via 99th Avenue or Grand Avenue (US-60)",
        "facts": [
            "Sun City is an unincorporated, age-restricted community managed by resident associations rather than a city government, which means most commercial buildings are HOA-run medical offices, banks, and small professional suites rather than corporate towers.",
            "Grand Avenue (US-60), the historic diagonal highway, runs directly through Sun City and is the main commercial corridor for the medical and professional offices that line it.",
            "Building stock here tends to be single-story and low-rise, built in the 1960s-80s Del Webb era, which changes the maintenance profile from what a mid-rise downtown tower needs.",
        ],
        "adjacent_note": "Sun City borders Youngtown to the south and Sun City West to the northwest, both reached via Grand Avenue or 99th Avenue.",
        "intro_extra": "Because Sun City is unincorporated and age-restricted, the property management landscape here looks different than in a standard incorporated city: resident associations and small management companies oversee the medical and professional buildings along Grand Avenue, rather than large commercial property firms. Service here is scoped around mobility-friendly common areas and a tenant mix weighted toward healthcare rather than corporate offices.",
    },
    "surprise": {
        "name": "Surprise",
        "drive": "about 20-25 minutes (roughly 12-16 miles) northwest via Bell Road or Grand Avenue",
        "facts": [
            "The Loop 303 corridor through Surprise is a defining piece of infrastructure distinct from Peoria's Loop 101 access, and it has drawn a wave of newer office and industrial construction along its frontage.",
            "The Prasada development near Bell Road and the 303 mixes retail, medical office, and professional suites in a single master-planned commercial node.",
            "Surprise Stadium and the adjacent Surprise Recreation Campus generate seasonal spikes in foot traffic each spring that put extra load on common-area cleaning schedules for nearby buildings.",
        ],
        "adjacent_note": "Surprise borders El Mirage to the southeast and Waddell to the south, both inside the same Bell Road / Loop 303 service corridor.",
        "intro_extra": "Surprise has seen some of the newest commercial construction in the West Valley along the Loop 303 corridor, which means many buildings here are recent enough that tenants expect a polished, contemporary standard rather than tolerating the wear patterns of an older property. That newer construction also means more glass and polished-concrete common areas, surfaces that show dust and streaking faster than older carpet-and-tile buildings.",
    },
    "el-mirage": {
        "name": "El Mirage",
        "drive": "about 10-15 minutes (roughly 7-10 miles) via Grand Avenue or Thunderbird Road",
        "facts": [
            "El Mirage's commercial footprint is concentrated along Grand Avenue (US-60) and Thunderbird Road, with a smaller inventory of standalone office and retail buildings than its larger neighbors.",
            "Because Grand Avenue cuts through El Mirage on a diagonal, several commercial parcels sit on irregular lots, which affects exterior common-area layout and entrance cleaning routes.",
            "The city's municipal and community campus area anchors a modest but steady cluster of professional office tenants near El Mirage Road.",
        ],
        "adjacent_note": "El Mirage sits between Surprise to the northwest and Youngtown to the southeast, both a short run down Grand Avenue.",
        "intro_extra": "El Mirage's commercial inventory is smaller and more modest than its larger neighbors, which means buildings here tend to be standalone or small multi-tenant properties rather than large office complexes. That changes the scope conversation: a building here is more likely to need a lean, tightly scoped service plan than the broader multi-service package a larger complex would carry.",
    },
    "youngtown": {
        "name": "Youngtown",
        "drive": "about 10 minutes (roughly 7-9 miles) via 111th Avenue or Grand Avenue",
        "facts": [
            "Youngtown was founded in 1954 as one of the first age-restricted communities in the country; the age restriction was lifted decades ago, so today it's a small, standard incorporated town rather than a retirement community.",
            "Commercial inventory is limited and concentrated along Grand Avenue and 111th Avenue, mostly small retail and professional suites rather than multi-story buildings.",
            "Its compact size means most commercial properties in Youngtown are within a few minutes of each other, which helps keep multi-stop service routes tight and predictable.",
        ],
        "adjacent_note": "Youngtown borders Sun City to the north and El Mirage to the west, both reachable via Grand Avenue.",
        "intro_extra": "Youngtown's commercial footprint is the smallest in our service area, and that's worth being upfront about rather than overselling. If your building is a small retail or professional space here, you likely don't need the multi-service program a larger complex would carry; you need a right-sized scope that doesn't pad the invoice with coverage the property doesn't use.",
    },
    "waddell": {
        "name": "Waddell",
        "drive": "about 20-25 minutes (roughly 14-18 miles) west via Northern Avenue or Cotton Lane",
        "facts": [
            "Waddell sits adjacent to White Tank Mountain Regional Park, and buildings here see more direct dust exposure during windstorms than properties closer to the urban core.",
            "The area is largely unincorporated and transitional between agricultural land and newer suburban development along the Cotton Lane corridor.",
            "Lower commercial density means many properties here are standalone buildings rather than multi-tenant complexes, which changes the scope of common-area work compared to a denser office park.",
        ],
        "adjacent_note": "Waddell borders Surprise to the north and Sun City West to the east, both reached via Cotton Lane or Bell Road.",
        "intro_extra": "Being closer to White Tank Mountain Regional Park than any other town in our service area, Waddell buildings deal with more direct desert exposure than properties closer to the urban core. That means entry glass and exterior common areas need a maintenance rhythm built around wind events, not just a fixed weekly schedule, since a single dust storm can undo a week's worth of upkeep in an afternoon.",
    },
    "sun-city-west": {
        "name": "Sun City West",
        "drive": "about 20 minutes (roughly 12-15 miles) via 99th Avenue, Grand Avenue, or Bell Road",
        "facts": [
            "Like Sun City, Sun City West is an unincorporated, age-restricted 55+ community developed by Del Webb starting in the late 1970s, with commercial buildings run by resident associations rather than a municipal government.",
            "R.H. Johnson Boulevard is the community's main internal spine, lined with medical offices, banks, and small professional buildings serving residents.",
            "The community borders open desert toward Hassayampa to the west, which means end-of-day dust accumulation on exterior glass and entryways is a more consistent maintenance factor here than in denser parts of the Valley.",
        ],
        "adjacent_note": "Sun City West borders Sun City to the southeast and Waddell to the south, both a short drive along Bell Road or 99th Avenue.",
        "intro_extra": "Like Sun City, Sun City West's commercial buildings are managed largely through resident associations rather than traditional commercial property firms, and the tenant base along R.H. Johnson Boulevard is weighted heavily toward medical and banking services serving an older-adult population. Combined with the community's proximity to open desert toward Hassayampa, that means our service plans here prioritize accessible, low-glare common areas and consistent entry-glass care over the higher-traffic patterns a downtown office building would need.",
    },
    "phoenix": {
        "name": "Phoenix",
        "drive": "about 15-20 minutes (roughly 10-14 miles) to the nearest northwest Phoenix commercial nodes via I-17 or Loop 101",
        "facts": [
            "The Deer Valley area, anchored by Deer Valley Airport, is a general-aviation and business-park hub with light-industrial and office buildings lining I-17 near Deer Valley Road.",
            "The Metrocenter area, a former regional mall site, is being repositioned into mixed-use commercial development along I-17, bringing a new wave of multi-tenant buildings into the market.",
            "I-17 (the Black Canyon Freeway) is the defining corridor for northwest Phoenix commercial property and is the same route our crews use to reach the area from Peoria.",
        ],
        "adjacent_note": "This part of northwest Phoenix borders Glendale to the west and Sun City to the northwest, both reached via Loop 101 or I-17.",
        "intro_extra": "Northwest Phoenix around Deer Valley mixes light-industrial and general-aviation business-park tenants with office space repositioned from older retail sites like Metrocenter. That mix means common areas here see more grit and debris tracked in from industrial tenants than a pure office building would, which changes how entry-mat and lobby-floor service gets scoped compared to the medical-office buildings a few miles away in Sun City.",
    },
}

TOWN_ORDER = ["glendale", "sun-city", "surprise", "el-mirage", "youngtown", "waddell", "sun-city-west", "phoenix"]
