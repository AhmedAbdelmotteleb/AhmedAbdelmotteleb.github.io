// Progressive enhancement only: the site is fully usable without this file.
document.documentElement.classList.add("js");

// Gallery prev/next buttons for the scroll-snap photo strip.
document.querySelectorAll("[data-gallery]").forEach(function (wrap) {
  var strip = wrap.querySelector(".gallery");
  var prev = wrap.querySelector("[data-prev]");
  var next = wrap.querySelector("[data-next]");
  if (!strip || !prev || !next) return;

  function step(dir) {
    var item = strip.querySelector("li");
    var amount = item ? item.getBoundingClientRect().width + 16 : strip.clientWidth * 0.8;
    strip.scrollBy({ left: dir * amount, behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
  }
  function update() {
    prev.disabled = strip.scrollLeft <= 2;
    next.disabled = strip.scrollLeft + strip.clientWidth >= strip.scrollWidth - 2;
  }
  prev.addEventListener("click", function () { step(-1); });
  next.addEventListener("click", function () { step(1); });
  strip.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
});
