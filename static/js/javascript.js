  // JS toggle sidebar
const currenPath = window.location.pathname;
const links = document.querySelectorAll(".step-item");

links.forEach(link => {
  const href = link.getAttribute("href");

  if(currenPath === href){
    link.classList.add("active");
  }
})