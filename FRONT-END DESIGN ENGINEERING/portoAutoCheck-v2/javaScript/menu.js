document.addEventListener("DOMContentLoaded", function() {
  const menuIcon = document.querySelector(".menu-icon");
  const sideMenu = document.querySelector("#sideMenu");
  const contentFrame = document.querySelector("#contentFrame");

  menuIcon.addEventListener("click", function() {
      sideMenu.classList.toggle("active");
      document.body.classList.toggle("menu-active");
  });

  const menuItems = document.querySelectorAll("#sideMenu ul li");

  menuItems.forEach(function(item) {
      if (item.id !== "logoutBtn") {
          item.addEventListener("click", function() {
              const page = item.dataset.page;
              if (page) {
                  contentFrame.src = page;
              }
          });
      } else {
          item.addEventListener("click", function() {
              logout();
          });
      }
  });

  function logout() {
      window.location.href = "login.html";
  }
});



