document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    sendBtn.addEventListener("click", () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            displayMessage("You", userMessage);
            userInput.value = "";

            // Simulate assistant response
            setTimeout(() => {
                const emotion = detectEmotion(userMessage);
                const assistantResponse = generateResponse(emotion);
                displayMessage("Assistant", assistantResponse);
            }, 1000);
        }
    });

    function displayMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.className = sender === "You" ? "user-message" : "assistant-message";
        messageElement.textContent = `${sender}: ${message}`;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
    }

    function detectEmotion(message) {
        // Placeholder for emotion detection logic
        if (message.includes("happy")) return "happy";
        if (message.includes("sad")) return "sad";
        return "neutral";
    }

    function generateResponse(emotion) {
        // Placeholder for response logic
        switch (emotion) {
            case "happy": return "I'm glad to hear that! What else is on your mind?";
            case "sad": return "I'm here for you. Would you like to talk about it?";
            default: return "Tell me more.";
        }
    }
});
