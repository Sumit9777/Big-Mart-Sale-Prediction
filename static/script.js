const showBtn = document.querySelector("#icon i"),
      menuList = document.querySelector(".header-section nav ul");

      showBtn.addEventListener("click" , () => {
        menuList.classList.toggle('show');
      })