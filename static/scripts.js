async function sendMessage() {
  const message = document.getElementById("message");
  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message.value }),
    });

    const data = await response.json();

    document.getElementById("response").textContent = data.response;
  } catch (error) {
    console.error("Error sending message:", error);
  }
}
