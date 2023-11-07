function scrollBanner() {
    var scrollPos;
    var headerText = document.querySelector('.header-paralax');
    scrollPos = window.scrollY;
  
    if (scrollPos <= 600) {
      headerText.style.transform = "translateY(" + (-scrollPos / 3) + "px" + ")";
      headerText.style.opacity = 1 - (scrollPos / 600);
    }
  }
  window.addEventListener('scroll', scrollBanner);