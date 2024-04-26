document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("loginForm");
  
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();
  
        // Permitir login sem verificar nome de usuário ou senha
        window.location.href = "popup.html";
    });
  
    const registerButton = document.getElementById("registerButton");
    registerButton.addEventListener("click", function() {
        // Redirecionar para a página de registro
        window.location.href = "registro.html";
    });
  });
  

