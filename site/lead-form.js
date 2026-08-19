(function () {
  "use strict";

  var UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"];
  var STORAGE_KEY = "qm_utm_params";

  function captureUtmParams() {
    var params = new URLSearchParams(window.location.search);
    var found = {};
    var hasAny = false;
    UTM_KEYS.forEach(function (key) {
      var value = params.get(key);
      if (value) {
        found[key] = value;
        hasAny = true;
      }
    });
    if (hasAny) {
      try {
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify(found));
      } catch (e) {
        /* sessionStorage unavailable (private browsing, etc.) — degrade silently */
      }
    }
  }

  function getStoredUtm() {
    try {
      var raw = sessionStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function setStatus(el, message, isError) {
    if (!el) return;
    el.textContent = message;
    el.hidden = false;
    el.className = "form-status " + (isError ? "form-status-error" : "form-status-success");
  }

  function handleSubmit(form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      var statusEl = form.querySelector("[data-form-status]");
      var submitBtn = form.querySelector('button[type="submit"]');
      var formData = new FormData(form);
      var utm = getStoredUtm();

      var payload = {
        zip: (formData.get("zip") || "").toString().trim(),
        customer: {
          company_name: (formData.get("company_name") || "").toString().trim(),
          first_name: (formData.get("first_name") || "").toString().trim(),
          last_name: (formData.get("last_name") || "").toString().trim(),
          phone: (formData.get("phone") || "").toString().replace(/\D/g, ""),
          email: (formData.get("email") || "").toString().trim(),
          address: "",
          service_address: "",
          notes: (formData.get("notes") || "").toString().trim(),
        },
        sqft: (formData.get("sqft") || "").toString().trim(),
        utm_source: utm.utm_source || "",
        utm_medium: utm.utm_medium || "",
        utm_campaign: utm.utm_campaign || "",
        utm_term: utm.utm_term || "",
        utm_content: utm.utm_content || "",
        page_url: window.location.href,
      };

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Sending...";
      }
      setStatus(statusEl, "", false);
      statusEl && (statusEl.hidden = true);

      fetch("/api/submit-lead", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      })
        .then(function (res) {
          return res.json().then(function (data) {
            return { ok: res.ok, data: data };
          });
        })
        .then(function (result) {
          if (result.ok) {
            form.reset();
            setStatus(
              statusEl,
              "Thanks — your request was submitted. We reply next business day.",
              false
            );
          } else {
            setStatus(
              statusEl,
              "We couldn't submit your request right now. Please call us or try again shortly.",
              true
            );
          }
        })
        .catch(function () {
          setStatus(
            statusEl,
            "We couldn't submit your request right now. Please call us or try again shortly.",
            true
          );
        })
        .finally(function () {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = "Request My Quote";
          }
        });
    });
  }

  captureUtmParams();

  document.addEventListener("DOMContentLoaded", function () {
    var forms = document.querySelectorAll("[data-lead-form]");
    forms.forEach(handleSubmit);
  });
})();
