---
layout: page
title: Home
description: "Personal website of Krishna Patel, PhD researcher at IIT Delhi focusing on molecular dynamics simulations."
permalink: /
---
<div class="not-prose grid gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-start">
  <div class="space-y-6">
    <p class="text-sm font-semibold uppercase tracking-widest text-muted">PhD Researcher &middot; Department of Chemical Engineering &middot; IIT Delhi</p>
    <h1 class="text-4xl font-semibold text-brand">Hi, I'm Krishna Patel.</h1>
    <p class="text-slate-700">
      I use atomistic simulations to study hydrogen storage in carbon materials.
      My current work covers graphene, CNTs, graphene&ndash;CNT frameworks, and other 2D carbon allotropes,
      with Python-based analysis.
    </p>
    <p class="text-sm font-medium uppercase tracking-[0.2em] text-accent">Molecular dynamics &middot; Carbon allotropes &middot; Research computing</p>
    <div class="flex flex-wrap gap-3">
      <a class="inline-flex items-center gap-2 rounded-full bg-accent px-5 py-2 text-sm font-semibold text-white transition hover:bg-brand focus:outline-none focus-visible:ring focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ '/cv/' | relative_url }}">
        View CV
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
      <h3 class="text-xl font-semibold text-brand">Recent publication</h3>
      <p class="mt-2 text-slate-700">
        "Effect of Graphene on the Conformation and Dynamics of Atactic Polystyrene in Toluene" was published in <em>Journal of Molecular Modeling</em>, 32(3), 75 (2026).
      </p>
      <p class="mt-3 text-sm text-slate-600">
        <a href="https://doi.org/10.1007/s00894-026-06655-1" class="text-accent hover:underline">DOI</a>
        ·
        <a href="https://rdcu.be/e4xyi" class="text-accent hover:underline">Shared-access link</a>
      </p>
    </article>
    <article class="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-sm">
      <h3 class="text-xl font-semibold text-brand">Manuscript under review</h3>
      <p class="mt-2 text-slate-700">
        "Role of Junction Topology and Pillar Configuration in Hydrogen Storage of Graphene&ndash;CNT
        Frameworks" is under review at <em>Diamond and Related Materials</em>.
      </p>
      <p class="mt-3 text-sm text-slate-600">
        <a href="{{ '/publications/' | relative_url }}" class="text-accent hover:underline">Publication details</a>
      </p>
    </article>
  </div>
</section>

<section class="not-prose">
  <div class="flex flex-wrap items-end justify-between gap-4">
    <div>
      <h2 class="text-2xl font-semibold text-brand">Research focus over time</h2>
    </div>
    <div class="flex items-center gap-2 pb-1 text-accent" aria-hidden="true">
      <svg class="h-5 w-8" viewBox="0 0 32 20" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M10 4L4 10M4 10L10 16M4 10H28" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" />
      </svg>
      <span class="text-xs font-semibold uppercase tracking-widest">Scroll</span>
    </div>
  </div>

  <div class="mt-7 snap-x snap-mandatory overflow-x-auto pb-4" style="direction: rtl;" aria-label="Scroll left through the research focus timeline">
    <ol class="flex min-w-max" style="direction: rtl;">
      <li class="w-[19rem] shrink-0 snap-start border-l border-slate-200 px-6 py-2 text-left" style="direction: ltr;">
        <p class="text-xs font-semibold uppercase tracking-widest text-accent">Current focus</p>
        <h3 class="mt-2 text-lg font-semibold text-brand">Machine-learned interatomic potentials</h3>
        <p class="mt-2 text-sm leading-relaxed text-slate-700">
          I am developing a DeePMD-based MLIP for lithium-decorated psi-graphene. I am also learning
          MACE and variational autoencoders for materials modelling.
        </p>
        <p class="mt-4 text-sm font-semibold text-accent">Jul 2026 &ndash; Present</p>
      </li>

      <li class="w-[19rem] shrink-0 snap-start border-l border-slate-200 px-6 py-2 text-left" style="direction: ltr;">
        <p class="text-xs font-semibold uppercase tracking-widest text-muted">Hydrogen storage</p>
        <h3 class="mt-2 text-lg font-semibold text-brand">Graphene and graphene&ndash;CNT frameworks</h3>
        <p class="mt-2 text-sm leading-relaxed text-slate-700">
          Junction topology, pillar density, accessible volume, adsorption energetics, and gravimetric
          or volumetric storage metrics in carbon architectures.
        </p>
        <p class="mt-4 text-sm font-semibold text-accent">2025 &ndash; Present</p>
      </li>

      <li class="w-[19rem] shrink-0 snap-start border-l border-slate-200 px-6 py-2 text-left" style="direction: ltr;">
        <p class="text-xs font-semibold uppercase tracking-widest text-muted">Polymer interfaces</p>
        <h3 class="mt-2 text-lg font-semibold text-brand">Polystyrene dynamics near graphene</h3>
        <p class="mt-2 text-sm leading-relaxed text-slate-700">
          Atomistic study of polymer conformation, mean-square displacement, diffusivity, and
          polymer&ndash;graphene interfacial dynamics in toluene.
        </p>
        <p class="mt-4 text-sm font-semibold text-accent">2022 &ndash; 2025</p>
      </li>

      <li class="w-[19rem] shrink-0 snap-start border-l border-slate-200 px-6 py-2 text-left" style="direction: ltr;">
        <p class="text-xs font-semibold uppercase tracking-widest text-muted">M.Tech foundation</p>
        <h3 class="mt-2 text-lg font-semibold text-brand">Binary hard-disk self-assembly</h3>
        <p class="mt-2 text-sm leading-relaxed text-slate-700">
          Event-driven molecular dynamics of ordered structures, phase behaviour, and kinetic arrest
          across composition, size ratio, and packing fraction.
        </p>
        <p class="mt-4 text-sm font-semibold text-accent">Aug 2019 &ndash; Apr 2021</p>
      </li>
    </ol>
  </div>
</section>

<section>
  <h2 class="text-2xl font-semibold text-brand">Academic service &amp; outreach</h2>
  <ul>
    <li>Institute Invigilator for JEE (Advanced) 2026, IIT Delhi (mock test: 16 May 2026; examination: 17 May 2026).</li>
    <li>Creator of the <a href="https://www.youtube.com/channel/UCLz7KTIBaCLX8iBMOHBMNVg" class="text-accent hover:underline">NanoscaleModeling</a> YouTube channel with tutorials on molecular dynamics fundamentals.</li>
  </ul>
</section>
