// toggle button

const navMenu = document.getElementById("nav-menu")
const navLink = document.querySelectorAll(".nav-link")
const hamburger = document.getElementById("hamburger")

hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("left-[0]")
    hamburger.classList.toggle('ri-close-large-line')
})
 // hamburger icon to indicate menu open and auto close navlinck menu  when one navLinck is clicked
    navLink.forEach(link => {
      link.addEventListener("click", () => {
        navMenu.classList.add("left-[-100%]");
        navMenu.classList.remove("left-[0]");
        hamburger.classList.remove("ri-close-large-line");
        hamburger.classList.add("ri-menu-line");
      });
    });

// SWAPER WRAPPER

  document.addEventListener('DOMContentLoaded', () => {
    const swiper = new Swiper('.swiper', {
      loop: true,
      speed: 400,
      spaceBetween: 30,
      grabCursor: true,
      autoplay: {
        delay: 3000,
        disableOnInteraction: false
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true
      }
    });
  });

  // Show scroll-up button after scrolling down
  const scrollUpBtn = () => {
    const scrollUpBtn = document.getElementById("scroll-up")
    if(this.scrollup >= 250) {
      scrollUpBtn.classList.remove("-bottom-1/2")
      scrollUpBtn.classList.add("bottom-4")
    } else{
      scrollUpBtn.classList.add("-bottom-1/2")
      scrollUpBtn.classList.remove("bottom-4")
    }

  }
  window.addEventListener("scroll", scrollUp)
  
// xhange background header
const scrollHeader = () => {
  const header = document.getElementById("navbar");
  
  if (window.scrollY >= 50) {
    header.classList.add("border-b", "border-yellow-500");
  } else {
    header.classList.remove("border-b", "border-yellow-500");
  }
};

window.addEventListener("scroll", scrollHeader);


// scroll section active link
const activeLink = () => {
  const sections = document.querySelectorAll("section");
  const navLinks = document.querySelectorAll(".nav-link");

  let current = "home";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    
    if (window.scrollY >= sectionTop - 60) {
      current = section.getAttribute("id"); // Fix: Properly get section ID
    }
  });

  navLinks.forEach((item) => {
    item.classList.remove("active");

    if (item.href.includes(current)) {
      item.classList.add("active"); // Fix: Corrected class name from "activate" to "active"
    }
  });
};

window.addEventListener("scroll", activeLink); // Fix: Corrected event listener syntax

// scroll reveal Animations
const sr = ScrollReveal({
  origin: "top",          // Animation starts from the top
  distance: "60px",       // Moves 60px into view
  duration: 2500,         // Animation lasts 2.5 seconds
  delay: 300,             // Starts after 300ms
  reset: true             // Animates every time you scroll back to it
});

sr.reveal('.home_data');  // Targets elements with class 'home_data'



  



