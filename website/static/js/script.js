const container = document.querySelector(".container");

document.querySelector(".open-navbar-icon").addEventListener("click", () => {
  container.classList.add("change");
});

document.querySelector(".close-navbar-icon").addEventListener("click", () => {
  container.classList.remove("change");
});

const colors = ["#6495ed", "#7fffd4", "#ffa07a", "#f08080", "#afeeee"];

let i = 0;
Array.from(document.querySelectorAll(".nav-link")).forEach(item => {
  item.style.cssText = `background-color: ${colors[i++ % colors.length]}`;
});

// Smooth scroll on nav-link clicks for internal anchors
document.querySelectorAll(".nav-link").forEach(link => {
  const href = link.getAttribute("href");
  if (href && href.startsWith("#")) {
    link.addEventListener("click", e => {
      e.preventDefault();
      const targetSection = document.querySelector(href);
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: "smooth" });
        container.classList.remove("change");
      }
    });
  }
});

// --- Start: Card Flipping Functionality (Revised) ---
document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('.card');

  cards.forEach(card => {
    
    const flipButtons = card.querySelectorAll('.navigation-button');

    flipButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Toggle the 'change' class on the card
        card.classList.toggle('change');
        console.log('Card flip triggered by:', this); // Debugging message to see which button was clicked
      });
    });
  });
});
