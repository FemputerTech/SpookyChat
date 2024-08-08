function toggleNavList() {
  const navList = document.querySelector(".nav-list");

  if (navList.style.display === "") {
    navList.style.display = "flex";
  } else {
    navList.style.display = "";
  }
}

async function sendMessage() {
  const userMessageInput = document.getElementById("message");
  const userMessageContent = userMessageInput.value;
  const userMessage = { content: userMessageContent, role: "user" };
  this.appendMessage(userMessage);
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
