async function login() {
    try {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const response = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username: username, password: password })
        });
        const data = await response.json();
        if (response.ok) {
            document.getElementById("login-container").style.display = "none";
            document.getElementById("chat-container").style.display = "block";
        } else {
            document.getElementById("login-message").textContent = data.message;
        }
    } catch (error) {
        document.getElementById("login-message").textContent = "Login failed: " + error.message;
    }
}

async function logout() {
    await fetch("/logout", { method: "POST" });
    document.getElementById("login-container").style.display = "block";
    document.getElementById("chat-container").style.display = "none";
    document.getElementById("chat-box").innerHTML = "";
}

async function sendMessage() {
    try {
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
        if (data.reply) {
            chatBox.innerHTML += `<p class="bot">Bot: ${data.reply}</p>`;
        } else if (data.error) {
            chatBox.innerHTML += `<p class="bot">Error: ${data.error}</p>`;
        }
        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        const chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += `<p class="bot">Error: ${error.message}</p>`;
    }
}

function startVoice() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.onresult = function(event) {
        document.getElementById("user-input").value = event.results[0][0].transcript;
        sendMessage();
    };
    recognition.start();
}