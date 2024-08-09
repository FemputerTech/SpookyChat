function toggleNavList() {
  const navList = document.querySelector(".nav-list");

  if (navList.style.display === "") {
    navList.style.display = "flex";
  } else {
    navList.style.display = "";
  }
}

function appendMessage(message) {
  const messageDisplay = document.querySelector(".message-display");
  const messageDiv = document.createElement("div");
  messageDiv.classList = "message-container";
  messageDisplay.appendChild(messageDiv);
  if (message.role === "user") {
    const userMessage = document.createElement("p");
    userMessage.classList.add("user-message");
    userMessage.textContent = `${message.content}`;
    messageDiv.appendChild(userMessage);
  } else {
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot-message");
    botMessage.textContent = `${message.content}`;
    messageDiv.appendChild(botMessage);
  }
}

async function sendMessage() {
  const userMessageInput = document.getElementById("message");
  const userMessageContent = userMessageInput.value;
  const userMessage = { content: userMessageContent, role: "user" };
  appendMessage(userMessage);
  userMessageInput.value = "";
  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userMessageContent }),
    });
    const data = await response.json();
    const botMessage = { content: data.response, role: "bot" };
    this.appendMessage(botMessage);
  } catch (error) {
    console.error("Error sending message:", error);
  }
}
