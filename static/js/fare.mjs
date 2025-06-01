document.addEventListener("DOMContentLoaded", () => {
  const sourceSelect = document.getElementById("source");
  const destSelect = document.getElementById("destination");
  const calcBtn = document.getElementById("calc-btn");

  calcBtn.addEventListener("click", async () => {
    const source = sourceSelect.value;
    const destination = destSelect.value;

    if (!source || !destination || source === destination) return;

    try {
      const res = await fetch("/dmrc-fare", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ source, destination })
      });

      const data = await res.json();

      const main = document.querySelector("main");
      main.innerHTML = `<div class="fare-fullscreen">₹${data.fare}</div>`;

    } catch (err) {
      document.body.innerHTML = `<div class="fare-fullscreen">❌ Network Error</div>`;
    }
  });
});
