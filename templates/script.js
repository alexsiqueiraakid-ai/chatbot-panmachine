const API_URL = "https://chatbot-panmachine.onrender.com/";
// ⬆️ troque pela URL real do seu Flask (Render / Railway / Fly.io)

const form = document.getElementById("user-input-form");
const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    // Mensagem do usuário
    chatBox.innerHTML += `
        <div class="message user-message">
            <span class="sender">Você:</span> ${message}
        </div>
    `;

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Resposta do bot (permite HTML)
        chatBox.innerHTML += `
            <div class="message bot-response">
                <span class="sender">Bot:</span> ${data.response}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `
            <div class="message bot-response">
                <span class="sender">Bot:</span> Erro ao conectar com o servidor.
            </div>
        `;
    }
});

