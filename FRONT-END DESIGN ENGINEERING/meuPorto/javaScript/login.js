document.addEventListener("DOMContentLoaded", function() {
  const loginForm = document.getElementById("loginForm");
  const loginMessage = document.getElementById("loginMessage");
  const loginButton = document.getElementById("loginButton");

  loginForm.addEventListener("submit", function(event) {
      event.preventDefault();

      const username = loginForm.elements["username"].value;
      const password = loginForm.elements["password"].value;

      // Verificar as credenciais 
      if (username === "usuario" && password === "senha") {
          // Login bem-sucedido, redirecionar para a página do menu
          window.location.href = "popup.html";
      } else {
          // Exibir mensagem de erro
          loginMessage.textContent = "Credenciais inválidas. Por favor, tente novamente.";
      }
  });

  const registerButton = document.getElementById("registerButton");
  registerButton.addEventListener("click", function() {
      // Redirecionar para a página de registro
      window.location.href = "registro.html";
  });
});

