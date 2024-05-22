//protótipo de chatbot
function sendMessage() {
  var userInput = document.getElementById("user-input");
  var message = userInput.value;
  
  if (message.trim() === "") {
    alert("Por favor, digite uma mensagem!");
    return;
  }

  var chatBox = document.getElementById("chat-box");
  var userMessage = document.createElement("div");
  userMessage.className = "message user";
  userMessage.innerHTML = "<strong>Você:</strong> " + message;
  chatBox.appendChild(userMessage);

  userInput.value = ""; // Limpa o campo de entrada após enviar a mensagem
}

