(function () {
  const storageKey = "bankfinder-theme";

  function getPreferredTheme() {
    return localStorage.getItem(storageKey) || "light";
  }

  function setTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);
    localStorage.setItem(storageKey, theme);
    const moon = document.querySelector(".theme-icon-moon");
    const sun = document.querySelector(".theme-icon-sun");
    if (moon && sun) {
      moon.classList.toggle("d-none", theme === "dark");
      sun.classList.toggle("d-none", theme !== "dark");
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    setTheme(getPreferredTheme());
    const btn = document.getElementById("themeToggle");
    if (btn) {
      btn.addEventListener("click", function () {
        const next = document.documentElement.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
        setTheme(next);
      });
    }
  });

  function showToast(message, variant) {
    const area = document.getElementById("toastArea");
    if (!area || typeof bootstrap === "undefined") {
      return;
    }
    const el = document.createElement("div");
    el.className = "toast align-items-center text-bg-" + (variant || "info") + " border-0";
    el.setAttribute("role", "alert");
    el.setAttribute("aria-live", "assertive");
    el.setAttribute("aria-atomic", "true");
    el.innerHTML =
      '<div class="d-flex">' +
      '<div class="toast-body">' +
      message +
      "</div>" +
      '<button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>' +
      "</div>";
    area.appendChild(el);
    const t = new bootstrap.Toast(el, { delay: 4000 });
    t.show();
    el.addEventListener("hidden.bs.toast", function () {
      el.remove();
    });
  }

  window.BankApp = {
    showToast: showToast,
    setTheme: setTheme,
    getPreferredTheme: getPreferredTheme,
  };
})();
