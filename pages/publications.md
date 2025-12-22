---
layout: page
title: Publications
permalink: /publications/
---

## Conference Presentations

### ICTN-KLC 2025
**International Conference on Trends in Nanoscience - Kerala Lalithakala Academy, Thrissur**

<div style="text-align: center; margin: 20px 0;">
  <img src="/assets/images/ICTN_Abstract_Page.png" alt="Optimizing Hydrogen Adsorption on Graphene Oxide" style="max-width: 90%; height: auto; border: 2px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  <p style="margin-top: 10px; font-style: italic; color: #555;">Optimizing Hydrogen Adsorption on Graphene Oxide</p>
</div>

Presented research on "Optimizing Hydrogen Adsorption on Graphene Oxide" at ICTN-KLC 2025, exploring computational approaches to enhance hydrogen storage capabilities.

---

### CompFlu 2025
**International Conference on Computational Fluid Dynamics - IISc Bangalore**

<div style="position: relative; max-width: 800px; margin: 20px auto; text-align: center;">
  <div class="carousel-container" style="position: relative; overflow: hidden; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <img id="carousel-img-1" class="carousel-image" src="/assets/images/Ankita_jayatiSarkar_Mukul_KrishnaPatel_Jagat_InJNTATAAuditoriumIISs.JPG" alt="CompFlu 2025 Group Photo" style="width: 100%; height: auto; display: block; transition: opacity 1s ease-in-out;">
    <img id="carousel-img-2" class="carousel-image" src="/assets/images/RandomClickInJNTATAAuditoriumIISc.JPG" alt="CompFlu 2025 at IISc Auditorium" style="width: 100%; height: auto; display: none; transition: opacity 1s ease-in-out; position: absolute; top: 0; left: 0;">
  </div>
  <p style="margin-top: 10px; font-style: italic; color: #555;">CompFlu 2025 Conference at IISc Bangalore</p>
</div>

<script>
(function() {
  let currentImage = 0;
  const images = [
    document.getElementById('carousel-img-1'),
    document.getElementById('carousel-img-2')
  ];
  
  function fadeTransition() {
    // Fade out current image
    images[currentImage].style.opacity = '0';
    
    setTimeout(function() {
      images[currentImage].style.display = 'none';
      
      // Move to next image
      currentImage = (currentImage + 1) % images.length;
      
      // Fade in next image
      images[currentImage].style.display = 'block';
      setTimeout(function() {
        images[currentImage].style.opacity = '1';
      }, 50);
    }, 1000);
  }
  
  // Initialize - set first image visible
  images[0].style.opacity = '1';
  images[0].style.display = 'block';
  
  // Start carousel - switch every 5 seconds
  setInterval(fadeTransition, 5000);
})();
</script>

Participated in CompFlu 2025, the International Conference on Computational Fluid Dynamics held at the prestigious Indian Institute of Science (IISc), Bangalore.

---

## Publications
*More publications coming soon...*
