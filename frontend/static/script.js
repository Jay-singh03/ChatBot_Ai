async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    if (!message) return;
    const chatBox = document.getElementById("chat-box");
    // Show user message
    chatBox.innerHTML += `<p class="user">You: ${message}</p>`;
    // Send to backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });
    const data = await response.json();
    // Show bot reply
    chatBox.innerHTML += `<p class="bot">Bot: ${data.reply}</p>`;
    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}

function startVoice() {
    const recognition = new webkitSpeechRecognition();
    recognition.onresult = function(event) {
        document.getElementById("user-input").value = event.results[0][0].transcript;
        sendMessage();
    };
    recognition.start();
}