const CRM_GET_FAQ_URL = "https://thequotemasters.com/crm_api/api.php?action=get_lead_faq";

module.exports = async function handler(req, res) {
  if (req.method !== "GET") {
    res.setHeader("Allow", "GET");
    return res.status(405).json({ ok: false, error: "Method not allowed" });
  }

  const token = process.env.CRM_API_TOKEN;
  if (!token) {
    console.error("get-faq: CRM_API_TOKEN is not configured");
    return res.status(500).json({ ok: false, error: "Server misconfiguration" });
  }

  try {
    const crmResponse = await fetch(CRM_GET_FAQ_URL, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const rawText = await crmResponse.text();
    let crmData;
    try {
      crmData = JSON.parse(rawText);
    } catch (e) {
      crmData = { raw: rawText };
    }

    if (!crmResponse.ok) {
      console.error("get-faq: CRM returned an error", crmResponse.status, crmData);
      return res.status(502).json({ ok: false, error: "CRM request failed" });
    }

    res.setHeader("Cache-Control", "public, max-age=300, stale-while-revalidate=600");
    return res.status(200).json({ ok: true, data: crmData });
  } catch (err) {
    console.error("get-faq: request to CRM failed", err);
    return res.status(502).json({ ok: false, error: "Unable to reach CRM" });
  }
};
