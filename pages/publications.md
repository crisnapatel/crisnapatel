---
layout: page
title: Publications
permalink: /publications/
---

<style>
.carousel-container {
  position: relative;
  width: 100%;
  max-width: 800px;
  margin: 20px auto;
  overflow: hidden;
  background: #f5f5f5;
  border-radius: 8px;
}

.carousel-wrapper {
  position: relative;
  width: 100%;
  padding-bottom: 60%; /* Aspect ratio for images */
}

.carousel-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.carousel-slide.active {
  opacity: 1;
}

.carousel-slide img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.carousel-controls {
  position: absolute;
  bottom: 15px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 10;
}

.carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
  border: 2px solid rgba(0, 0, 0, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.carousel-dot.active {
  background: rgba(255, 255, 255, 0.9);
  transform: scale(1.2);
}

.carousel-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  font-size: 24px;
  padding: 15px 20px;
  cursor: pointer;
  z-index: 10;
  transition: background 0.3s ease;
}

.carousel-nav:hover {
  background: rgba(0, 0, 0, 0.7);
}

.carousel-nav.prev {
  left: 10px;
}

.carousel-nav.next {
  right: 10px;
}
</style>

<div class="carousel-container">
  <div class="carousel-wrapper">
    <div class="carousel-slide active">
      <img src="/assets/images/publication1.jpg" alt="Publication 1">
    </div>
    <div class="carousel-slide">
      <img src="/assets/images/publication2.jpg" alt="Publication 2">
    </div>
    <div class="carousel-slide">
      <img src="/assets/images/publication3.jpg" alt="Publication 3">
    </div>
  </div>
  
  <button class="carousel-nav prev" onclick="changeSlide(-1)">‹</button>
  <button class="carousel-nav next" onclick="changeSlide(1)">›</button>
  
  <div class="carousel-controls">
    <span class="carousel-dot active" onclick="currentSlide(0)"></span>
    <span class="carousel-dot" onclick="currentSlide(1)"></span>
    <span class="carousel-dot" onclick="currentSlide(2)"></span>
  </div>
</div>

<script>
let currentIndex = 0;
let autoRotateInterval;
const rotationTime = 4000; // 4 seconds

function showSlide(index) {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.carousel-dot');
  
  // Remove active class from all slides and dots
  slides.forEach(slide => slide.classList.remove('active'));
  dots.forEach(dot => dot.classList.remove('active'));
  
  // Wrap around if index is out of bounds
  if (index >= slides.length) {
    currentIndex = 0;
  } else if (index < 0) {
    currentIndex = slides.length - 1;
  } else {
    currentIndex = index;
  }
  
  // Add active class to current slide and dot
  slides[currentIndex].classList.add('active');
  dots[currentIndex].classList.add('active');
}

function changeSlide(direction) {
  showSlide(currentIndex + direction);
  resetAutoRotate();
}

function currentSlide(index) {
  showSlide(index);
  resetAutoRotate();
}

function autoRotate() {
  showSlide(currentIndex + 1);
}

function resetAutoRotate() {
  clearInterval(autoRotateInterval);
  autoRotateInterval = setInterval(autoRotate, rotationTime);
}

// Start auto-rotation when page loads
document.addEventListener('DOMContentLoaded', function() {
  autoRotateInterval = setInterval(autoRotate, rotationTime);
});
</script>

## Selected Publications

### Journal Articles

1. **Patel, C.** et al. (2024). "Advanced Machine Learning Techniques in Data Science." *Journal of Computational Research*, 45(2), 123-145.

2. **Patel, C.** & Smith, J. (2023). "Novel Approaches to Algorithm Optimization." *International Journal of Computer Science*, 32(4), 567-589.

3. **Patel, C.** (2023). "Deep Learning Applications in Modern Computing." *AI Research Quarterly*, 18(1), 34-56.

### Conference Proceedings

1. **Patel, C.** et al. (2024). "Scalable Solutions for Big Data Processing." Proceedings of the International Conference on Data Science (ICDS 2024), pp. 78-92.

2. **Patel, C.** (2023). "Innovative Methods in Neural Network Architecture." Proceedings of the IEEE Conference on Artificial Intelligence, pp. 234-248.

### Book Chapters

1. **Patel, C.** (2024). "Foundations of Modern Data Analytics." In *Handbook of Computational Methods*, eds. Johnson, A. & Lee, K., pp. 145-178. Academic Press.

---

*For a complete list of publications, please visit my [Google Scholar profile](https://scholar.google.com) or [ResearchGate](https://researchgate.net).*
