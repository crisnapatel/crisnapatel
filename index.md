---
layout: page
title: Home
description: "Personal website of Krishna Patel, PhD student at IIT Delhi focusing on molecular dynamics simulations."
permalink: /
---
<div class="not-prose grid gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-start">
  <div class="space-y-6">
    <p class="text-sm font-semibold uppercase tracking-widest text-muted">PhD Student · Department of Chemical Engineering · IIT Delhi</p>
    <h1 class="text-4xl font-semibold text-brand">Hi, I'm Krishna Patel.</h1>
    <p class="text-slate-700">
      I use atomic scale simulation to sudy hydrogen storage in various carbon-based materials.
      My current work focuses on hydrogen storage in Graphene Oxide and Graphene-CNT pillared framework materials.
    </p>
    <div class="flex flex-wrap gap-3">
      <a class="inline-flex items-center gap-2 rounded-full bg-accent px-5 py-2 text-sm font-semibold text-white transition hover:bg-brand focus:outline-none focus-visible:ring focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ '/assets/cv.pdf' | relative_url }}">
        Download CV
      </a>
      <a class="inline-flex items-center gap-2 rounded-full border border-accent px-5 py-2 text-sm font-semibold text-accent transition hover:bg-accent/10 focus:outline-none focus-visible:ring focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ '/contact/' | relative_url }}">
        Contact me
      </a>
    </div>
  </div>
  <figure class="mx-auto max-w-xs overflow-hidden rounded-3xl border border-slate-200 shadow-lg">
    <img src="{{ '/assets/images/krishna-patel.jpg' | relative_url }}" alt="Portrait of Krishna Patel" class="h-full w-full object-cover" />
    <figcaption class="bg-slate-100 px-4 py-3 text-sm text-slate-600">Capturing a quiet moment in the lab at IIT Delhi.</figcaption>
  </figure>
</div>

<section>
  <h2 class="text-2xl font-semibold text-brand">Recent highlights</h2>
  <div class="grid gap-6 md:grid-cols-2">
    <article class="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-sm">
      <h3 class="text-xl font-semibold text-brand">Hydrogen storage on modified graphene and CNTs</h3>
      <p class="mt-2 text-slate-700">
        Exploring how GO sheet size and oxidation ratio change adsorption capacity of GO using grand canonical Monte Carlo insertion & classical molecular dynamics simulation with LAMMPS.
      </p>
    </article>
    <article class="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-sm">
      <h3 class="text-xl font-semibold text-brand">Polystyrene oligomers in toluene</h3>
      <p class="mt-2 text-slate-700">
        Studying chain dimensions and diffusivity in the presence of graphene interfaces using Materials Studio.
      </p>
    </article>
  </div>
</section>

<section>
  <h2 class="text-2xl font-semibold text-brand">Teaching & outreach</h2>
  <ul>
    <li>Teaching Assistant for CLL113 (Numerical Methods) at IIT Delhi (year 2023, 2024, 2025).</li>
    <li>Creator of the <a href="https://www.youtube.com/channel/UCLz7KTIBaCLX8iBMOHBMNVg" class="text-accent hover:underline">NanoscaleModeling</a> YouTube channel with tutorials on molecular dynamics fundamentals.</li>
  </ul>
</section>

<section>
  <h2 class="text-2xl font-semibold text-brand">Experience</h2>
  <div class="grid gap-4 md:grid-cols-2">
    <div>
      <h3 class="font-semibold text-brand">Simulation</h3>
      <p>LAMMPS, Materials Studio, GROMACS, NAMD</p>
    </div>
    <div>
      <h3 class="font-semibold text-brand">Analysis</h3>
      <p>MDAnalysis, OVITO, VMD, pandas, numpy, matplotlib</p>
    </div>
    <div>
      <h3 class="font-semibold text-brand">Force fields & modelling</h3>
      <p>ReaxFF, AIREBO, COMPASSII (Materials Studio)</p>
    </div>
    <div>
      <h3 class="font-semibold text-brand">Others</h3>
      <p>Conda, Docker, Jekyll, GitHub Pages, HPC (MPI/CUDA builds)</p>
    </div>
  </div>
</section>
