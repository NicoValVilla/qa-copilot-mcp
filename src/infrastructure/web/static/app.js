const form = document.querySelector("#ticket-form");
const statusLabel = document.querySelector("#status");
const results = document.querySelector("#results");
const buttons = document.querySelectorAll("button[data-endpoint]");

function ticketPayload() {
  const data = new FormData(form);
  return {
    titulo: data.get("titulo"),
    descripcion: data.get("descripcion"),
    tipo: data.get("tipo"),
  };
}

function renderListCard(title, items) {
  return `
    <article class="result-card">
      <h3>${title}</h3>
      <ul>${items.map((item) => `<li>${item}</li>`).join("")}</ul>
    </article>
  `;
}

function renderResult(title, payload) {
  if (payload.nivel) {
    results.innerHTML = `
      <article class="result-card">
        <span class="badge">${payload.nivel}</span>
        <h3>${title}</h3>
        <p>${payload.explicacion}</p>
      </article>
    `;
    return;
  }

  const cards = Object.entries(payload).map(([key, value]) => {
    const label = key.replaceAll("_", " ");
    return renderListCard(label.charAt(0).toUpperCase() + label.slice(1), value);
  });
  results.innerHTML = cards.join("");
}

async function runTool(endpoint, title) {
  statusLabel.textContent = "Ejecutando MCP";
  buttons.forEach((button) => {
    button.disabled = true;
  });

  try {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(ticketPayload()),
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(error);
    }

    const payload = await response.json();
    renderResult(title, payload);
    statusLabel.textContent = "Resultado generado";
  } catch (error) {
    results.innerHTML = `
      <article class="result-card empty">
        <h3>Error</h3>
        <p>${error.message}</p>
      </article>
    `;
    statusLabel.textContent = "Error";
  } finally {
    buttons.forEach((button) => {
      button.disabled = false;
    });
  }
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    runTool(button.dataset.endpoint, button.dataset.title);
  });
});
