---
layout: page
title: Publications
permalink: /publications/
description: "Publications and presentations."
subtitle: "Curated selection of journal articles, conference papers, and talks."
---
> **Note:** Entries below summarise currently shareable work. 

## Journal manuscripts in preparation
- Hydrogen adsorption on functionalized graphene/CNT heterostructures. 
- Polymer dimention and diffusivity near graphene interfaces (submitted).

## Conference presentations

### 2025

- **K. K. Patel** and J. Sarkar, "Impact of Graphene on the Conformation and Dynamics of Atactic Polystyrene in Toluene," *CompFlu 2025: Annual International Meeting on Complex Fluids and Soft Matter in India*, J. N. Tata Auditorium, Indian Institute of Science (IISc), Bangalore, India, 13–17 December 2025. (Flash talk & Poster)

- **K. K. Patel** and J. Sarkar, Poster presentation at *3rd International Conference on Thin Films and Nanotechnology—Knowledge, Leadership and Commercialization (ICTN-KLC 2025)*, IIT Delhi, India, 11–13 December 2025.

- **K. K. Patel**\*, N. Singh\*, and J. Sarkar, "Simulation-based Study of Hydrogen Production and Storage," *ChemRD2 Symposium*, Department of Chemical Engineering, IIT Delhi, India, 27–28 November 2025. (Poster; \*Equal contribution)

### 2024

- Presented a poster on *polystyrene dimensions and diffusivity* at Soft Matter Meet-2024 organised by School of Natural Sciences at Shiv Nadar University, Delhi NCR.

---

## Conference Gallery

<div class="not-prose">
  <section class="mt-12">
    <h3 class="text-xl font-semibold text-brand mb-6">ICTN-KLC 2025 — IIT Delhi</h3>
    <div class="flex justify-center">
      <figure class="rounded-2xl overflow-hidden border border-slate-200 shadow-sm" style="max-width: 90%;">
        <img src="{{ '/assets/conferences/ICTN_Abstract_Page.png' | relative_url }}" alt="Poster on Optimizing Hydrogen Adsorption on Graphene Oxide" class="w-full h-auto" />
        <figcaption class="bg-slate-50 px-4 py-3 text-sm text-slate-600 text-center">"Optimizing Hydrogen Adsorption on Graphene Oxide" presented at ICTN-KLC 2025</figcaption>
      </figure>
    </div>
  </section>

  <section class="mt-12">
    <h3 class="text-xl font-semibold text-brand mb-6">CompFlu 2025 — IISc Bangalore</h3>
    <div class="flex justify-center">
      <div class="carousel-container rounded-2xl overflow-hidden border border-slate-200 shadow-sm" style="position: relative; max-width: 800px; width: 100%;">
        <img class="carousel-image" src="{{ '/assets/conferences/PresentingFlashTak.JPG' | relative_url }}" alt="Presenting flash talk at CompFlu 2025" style="width: 100%; height: auto; display: block;" data-caption="Presenting flash talk at CompFlu 2025, IISc Bangalore" />
        <img class="carousel-image" src="{{ '/assets/conferences/Presenting_Poster.JPG' | relative_url }}" alt="Presenting poster at CompFlu 2025" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="Presenting poster at CompFlu 2025" />
        <img class="carousel-image" src="{{ '/assets/conferences/Ankita_jayatiSarkar_Mukul_KrishnaPatel_Jagat_InJNTATAAuditoriumIISs.JPG' | relative_url }}" alt="With labmates at J. N. Tata Auditorium" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="With labmates at J. N. Tata Auditorium, IISc" />
        <img class="carousel-image" src="{{ '/assets/conferences/RandomClickInJNTATAAuditoriumIISc.JPG' | relative_url }}" alt="Attending sessions at CompFlu 2025" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="Attending sessions at CompFlu 2025" />
        <img class="carousel-image" src="{{ '/assets/conferences/Jagat_Ankita_Sarkar_Krishna_Mukul_IISc_Iconic_Building_Front.JPG' | relative_url }}" alt="Group photo in front of IISc iconic building" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="With Prof. Jayati Sarkar and labmates at IISc iconic building" />
        <img class="carousel-image" src="{{ '/assets/conferences/Krishna_Ankita_Sarkar_Mukul_Jagat_IISc_Chem_Eng_Dept_front.JPG' | relative_url }}" alt="At IISc Chemical Engineering Department" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="At Chemical Engineering Department, IISc" />
        <img class="carousel-image" src="{{ '/assets/conferences/IISc_Iconic_Building_Front.jpeg' | relative_url }}" alt="IISc iconic building front view" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="IISc iconic building - Front view" />
        <img class="carousel-image" src="{{ '/assets/conferences/IISc_Iconic_Building_Side.jpeg' | relative_url }}" alt="IISc iconic building side view" style="width: 100%; height: auto; display: none; position: absolute; top: 0; left: 0;" data-caption="IISc iconic building - Side view" />
        <figcaption id="carousel-caption" class="bg-slate-50 px-4 py-3 text-sm text-slate-600 text-center">Presenting flash talk at CompFlu 2025, IISc Bangalore</figcaption>
      </div>
    </div>
  </section>
</div>

<script>
(function() {
  const images = document.querySelectorAll('.carousel-image');
  const caption = document.getElementById('carousel-caption');
  let currentIndex = 0;

  function showNextImage() {
    // Fade out current image
    images[currentIndex].style.opacity = '0';
    images[currentIndex].style.transition = 'opacity 1s ease-in-out';
    
    setTimeout(function() {
      images[currentIndex].style.display = 'none';
      
      // Move to next image
      currentIndex = (currentIndex + 1) % images.length;
      
      // Fade in next image
      images[currentIndex].style.display = 'block';
      images[currentIndex].style.opacity = '0';
      setTimeout(function() {
        images[currentIndex].style.opacity = '1';
        // Update caption
        if (caption && images[currentIndex].dataset.caption) {
          caption.textContent = images[currentIndex].dataset.caption;
        }
      }, 50);
    }, 1000);
  }

  // Initialize first image
  images[0].style.opacity = '1';
  images[0].style.display = 'block';

  // Start carousel - rotate every 7 seconds
  setInterval(showNextImage, 7000);
})();
</script>
