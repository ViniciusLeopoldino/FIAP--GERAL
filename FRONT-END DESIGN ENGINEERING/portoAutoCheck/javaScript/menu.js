function changeContent(contentId) {
    var contents = document.getElementsByClassName('conteudo');
    for (var i = 0; i < contents.length; i++) {
        contents[i].style.display = 'none';
    }
    document.getElementById(contentId).style.display = 'block';
}

function logout() {
    // Fazer logout, redirecionar para a página de login
    window.location.href = "login.html";
}




