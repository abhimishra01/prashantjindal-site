/* Shared behavior for all three options. Content is fully visible without JS.
   Motion runs only when the user allows motion. */
(function () {
  var doc = document.documentElement;
  var motionOK = window.matchMedia && window.matchMedia("(prefers-reduced-motion: no-preference)").matches;
  var hasIO = "IntersectionObserver" in window;

  // 1. Reveal on scroll
  if (motionOK && hasIO) {
    var rev = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); rev.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    document.querySelectorAll("[data-reveal]").forEach(function (el) { rev.observe(el); });
  }

  // 2. Count-up figures. The final value is already in the HTML.
  if (motionOK && hasIO) {
    var cnt = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        cnt.unobserve(e.target);
        var el = e.target, raw = el.textContent;
        var target = parseFloat(raw.replace(/,/g, ""));
        if (isNaN(target)) return;
        var dec = (raw.split(".")[1] || "").length, comma = raw.indexOf(",") > -1;
        var t0 = null, dur = 1400;
        function fmt(v) {
          var s = v.toFixed(dec);
          return comma ? Number(s).toLocaleString("en-US", { minimumFractionDigits: dec }) : s;
        }
        function step(t) {
          if (!t0) t0 = t;
          var p = Math.min(1, (t - t0) / dur), k = 1 - Math.pow(1 - p, 4);
          el.textContent = p < 1 ? fmt(target * k) : raw;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.6 });
    document.querySelectorAll("[data-count]").forEach(function (el) { cnt.observe(el); });
  }

  // 3. Section index highlight (option 2)
  var index = document.querySelector(".index");
  if (index && hasIO) {
    var links = {};
    index.querySelectorAll("a").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        Object.keys(links).forEach(function (k) { links[k].removeAttribute("aria-current"); });
        var a = links[e.target.id];
        if (a) a.setAttribute("aria-current", "true");
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    Object.keys(links).forEach(function (id) { var s = document.getElementById(id); if (s) spy.observe(s); });
  }

  // 4. Timeline fill (option 2): light up steps as they pass the middle of the screen
  var steps = document.querySelectorAll(".t-step");
  if (steps.length && hasIO && motionOK) {
    var tl = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) e.target.classList.add("lit"); });
    }, { rootMargin: "0px 0px -45% 0px" });
    steps.forEach(function (s) { tl.observe(s); });
  } else {
    steps.forEach(function (s) { s.classList.add("lit"); });
  }

  // 5. Career rail buttons (option 3)
  var rail = document.querySelector(".rail-x");
  if (rail) {
    document.querySelectorAll(".rb").forEach(function (b) {
      b.addEventListener("click", function () {
        var card = rail.querySelector("li");
        var w = card ? card.getBoundingClientRect().width + 16 : 300;
        rail.scrollBy({ left: w * Number(b.getAttribute("data-dir")), behavior: motionOK ? "smooth" : "auto" });
      });
    });
  }

  // 6. Spotlight on cards (option 3)
  if (motionOK && window.matchMedia("(hover: hover)").matches) {
    document.querySelectorAll(".wcard").forEach(function (c) {
      c.addEventListener("pointermove", function (ev) {
        var r = c.getBoundingClientRect();
        c.style.setProperty("--x", (ev.clientX - r.left) + "px");
        c.style.setProperty("--y", (ev.clientY - r.top) + "px");
      });
    });
  }
})();
