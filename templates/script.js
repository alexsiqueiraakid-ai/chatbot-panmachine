const API_URL = "https://chatbot-panmachine.onrender.com/";

const form = document.getElementById('user-input-form');
const input = document.getElementById('user-input');
const responses = document.getElementById('responses');
const chatBox = document.getElementById('chat-box');
const micBtn = document.getElementById('mic-btn');

/* ---------- RECONHECIMENTO DE VOZ ---------- */
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.lang = 'pt-BR';

    micBtn.addEventListener('click', () => {
        recognition.start();
        micBtn.textContent = "🔴";
    });

    recognition.onresult = (event) => {
        input.value = event.results[0][0].transcript;
        micBtn.textContent = "🎤";
    };

    recognition.onend = () => {
        micBtn.textContent = "🎤";
    };
} else {
    micBtn.style.display = "none";
}

/* ---------- CHAT ---------- */
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const userMessage = input.value.trim();
    if (!userMessage) return;

    responses.innerHTML += `
        <div class="message user-message">
            <span class="sender">Você:</span> ${userMessage}
        </div>
    `;

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();

        responses.innerHTML += `
            <div class="message bot-response">
                <span class="sender">Panmachine:</span> ${data.response}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch {
        responses.innerHTML += `
            <div class="message bot-response">
                Erro ao conectar com o servidor.
            </div>
        `;
    }
});



