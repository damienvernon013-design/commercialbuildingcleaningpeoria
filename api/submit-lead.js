const CRM_PUSH_LEAD_URL = "https://thequotemasters.com/crm_api/api.php?action=push_lead";

// Peoria Building Cleaning Co's assigned industry code and default number of
// quotes requested per lead, per the CRM-QM API documentation for this domain.
const INDUSTRY_CODE = 23;
const DEFAULT_NUMBER_OF_QUOTES = "2";

function isNonEmptyString(value) {
  return typeof value === "string" && value.trim().length > 0;
}

function sanitizeString(value, maxLength) {
  if (typeof value !== "string") return "";
  return value.trim().slice(0, maxLength);
}

function validatePayload(body) {
  const errors = [];
  const customer = body && typeof body.customer === "object" ? body.customer : {};

  if (!isNonEmptyString(body.zip) || !/^\d{5}$/.test(body.zip.trim())) {
    errors.push("zip must be a 5-digit string");
  }
  if (!isNonEmptyString(customer.first_name)) errors.push("customer.first_name is required");
  if (!isNonEmptyString(customer.last_name)) errors.push("customer.last_name is required");
  if (!isNonEmptyString(customer.email) || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(customer.email)) {
    errors.push("customer.email must be a valid email");
  }
  if (!isNonEmptyString(customer.phone) || customer.phone.replace(/\D/g, "").length < 10) {
    errors.push("customer.phone must be at least 10 digits");
  }

  return errors;
}

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }

  const token = process.env.CRM_API_TOKEN;
  if (!token) {
    console.error("submit-lead: CRM_API_TOKEN is not configured");
    return res.status(500).json({ ok: false, error: "Server misconfiguration" });
  }

  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch (e) {
      return res.status(400).json({ ok: false, error: "Invalid JSON body" });
    }
  }
  if (!body || typeof body !== "object") {
    return res.status(400).json({ ok: false, error: "Invalid request body" });
  }

  const validationErrors = validatePayload(body);
  if (validationErrors.length > 0) {
    return res.status(400).json({ ok: false, error: "Validation failed", details: validationErrors });
  }

  const customer = body.customer || {};

  const crmPayload = {
    zip: sanitizeString(body.zip, 10),
    customer: {
      company_name: sanitizeString(customer.company_name, 200),
      first_name: sanitizeString(customer.first_name, 100),
      last_name: sanitizeString(customer.last_name, 100),
      position: sanitizeString(customer.position, 100),
      phone: sanitizeString(customer.phone, 20).replace(/\D/g, ""),
      email: sanitizeString(customer.email, 200),
      email2: "",
      address: sanitizeString(customer.address, 300),
      service_address: sanitizeString(customer.service_address || customer.address, 300),
      notes: sanitizeString(customer.notes, 2000),
    },
    industry: INDUSTRY_CODE,
    questions: Array.isArray(body.questions) ? body.questions : [],
    appointments: Array.isArray(body.appointments) ? body.appointments : [],
    number_of_quotes: sanitizeString(body.number_of_quotes, 10) || DEFAULT_NUMBER_OF_QUOTES,
    utm_source: sanitizeString(body.utm_source, 255),
  };

  try {
    const crmResponse = await fetch(CRM_PUSH_LEAD_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(crmPayload),
    });

    const rawText = await crmResponse.text();
    let crmData;
    try {
      crmData = JSON.parse(rawText);
    } catch (e) {
      crmData = { raw: rawText };
    }

    if (!crmResponse.ok) {
      console.error("submit-lead: CRM rejected the lead", crmResponse.status, crmData);
      return res.status(502).json({ ok: false, error: "CRM rejected the request" });
    }

    return res.status(200).json({ ok: true, data: crmData });
  } catch (err) {
    console.error("submit-lead: request to CRM failed", err);
    return res.status(502).json({ ok: false, error: "Unable to reach CRM" });
  }
};
