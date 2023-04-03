const elements = document.querySelectorAll('.invisible');
const windowHeight = window.innerHeight;

function handleIntersect(entries, observer) {
  entries.forEach((entry) => {
    if (entry.intersectionRatio > 0.5) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}

const observer = new IntersectionObserver(handleIntersect);

elements.forEach((element) => {
  observer.observe(element);
});

window.addEventListener('resize', () => {
  windowHeight = window.innerHeight;
});

function animate() {
  elements.forEach((element) => {
    if (element.classList.contains('visible')) return;

    const elementTop = element.getBoundingClientRect().top;
    if (elementTop < windowHeight) {
      element.classList.add('slide-in');
    }
  });

  requestAnimationFrame(animate);
}

animate();
