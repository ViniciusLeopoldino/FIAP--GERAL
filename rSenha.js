const saveButton = document.getElementById("saveButton");
saveButton.addEventListener("click", function() {
// Redirecionar para a página de registro
window.location.href = "login.html";
});

const returnButton = document.getElementById("returnButton");
returnButton.addEventListener("click", function() {
    // Redirecionar para a página de login
    window.location.href = "login.html";
});