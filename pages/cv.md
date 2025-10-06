---
layout: page
title: null
permalink: /cv/
description: "Curriculum vitae of Krishna Kumar Patel, PhD student at IIT Delhi focusing on molecular simulations and hydrogen storage."
meta:
  title: "Krishna Kumar Patel - Curriculum Vitae"
  description: "Education, skills, and research experience of Krishna Patel, PhD student in Chemical Engineering at IIT Delhi."
extra_head: |
  <style>
    @media print {
      header,
      nav,
      .site-footer,
      .skip-link,
      button,
      .print-hidden {
        display: none !important;
      }
      body {
        color: #0f172a;
        font-size: 11pt;
      }
      a {
        color: #0f172a !important;
        text-decoration: none !important;
      }
      main {
        padding: 0 !important;
      }
    }
  </style>
---

<div class="not-prose space-y-12">
  <div class="flex flex-wrap items-center justify-between gap-6 rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
    <div class="space-y-2">
      <h1 class="text-3xl font-semibold text-brand">Curriculum Vitae</h1>
      <p class="text-sm uppercase tracking-widest text-muted">{{ site.role_line }}</p>
      <p class="text-base text-slate-600">
        Krishna Kumar Patel - molecular simulation researcher specializing in carbonaceous materials, polymer–solvent systems, and hydrogen storage.
      </p>
    </div>
    <a
      class="inline-flex items-center gap-2 rounded-full bg-accent px-5 py-2 text-sm font-semibold text-white shadow transition hover:bg-brand focus:outline-none focus-visible:ring focus-visible:ring-accent focus-visible:ring-offset-2"
      href="{{ '/assets/cv.pdf' | relative_url }}"
    >
      <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 8.25H7.5A2.25 2.25 0 005.25 10.5v9A2.25 2.25 0 007.5 21.75h9a2.25 2.25 0 002.25-2.25v-9A2.25 2.25 0 0016.5 8.25H15" />
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l3 3 3-3m-3 3V2.25" />
      </svg>
      Download PDF
    </a>
  </div>

  <section>
    <h2 class="text-2xl font-semibold text-brand">Education</h2>
    <ol class="mt-6 space-y-6">
      <li class="grid gap-4 md:grid-cols-[minmax(0,160px)_1fr] md:items-start">
        <div class="rounded-2xl bg-slate-100 px-4 py-3 text-center text-sm font-semibold text-slate-700">Jun 2021 – Present</div>
        <div class="space-y-2 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <h3 class="text-xl font-semibold text-brand">Doctor of Philosophy (PhD), Chemical Engineering</h3>
          <p class="text-sm font-medium text-slate-600">Indian Institute of Technology Delhi, India</p>
          <p class="text-sm text-slate-600">Advisor: Prof. Jayati Sarkar</p>
          <p class="text-sm text-slate-600">Focus: nanoscale simulations, hydrogen storage, carbonaceous materials.</p>
        </div>
      </li>
      <li class="grid gap-4 md:grid-cols-[minmax(0,160px)_1fr] md:items-start">
        <div class="rounded-2xl bg-slate-100 px-4 py-3 text-center text-sm font-semibold text-slate-700">Aug 2019 – Apr 2021</div>
        <div class="space-y-2 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <h3 class="text-xl font-semibold text-brand">Master of Technology (M.Tech), Chemical Engineering</h3>
          <p class="text-sm font-medium text-slate-600">National Institute of Technology Warangal, India</p>
          <p class="text-sm text-slate-600">CGPA: 7.4/10 </p>
          <p class="text-sm text-slate-600">Event-Driven Molecular Dynamics Simulation of Self Assembly of Binary Hard Disks.</p>
        </div>
      </li>
      <li class="grid gap-4 md:grid-cols-[minmax(0,160px)_1fr] md:items-start">
        <div class="rounded-2xl bg-slate-100 px-4 py-3 text-center text-sm font-semibold text-slate-700">2015 – 2019</div>
        <div class="space-y-2 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
          <h3 class="text-xl font-semibold text-brand">Bachelor of Technology (B.Tech), Chemical Engineering</h3>
          <p class="text-sm font-medium text-slate-600">Guru Ghasidas University, Bilaspur, India</p>
          <p class="text-sm text-slate-600">CGPA: 8.4/10 </p>
          <p class="text-sm text-slate-600">BTP: Reactive extraction of Gallic acid with Tri-n-Butyl Phosphate using rice bran oil and n-Butanol as diluents.</p>
        </div>
      </li>
    </ol>
  </section>

<section class="mt-12 grid gap-6 md:grid-cols-2">
  <div class="space-y-3 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
    <h3 class="text-xl font-semibold text-brand border-b pb-2">Research Skills</h3>
    <ul class="mt-3 list-disc list-inside space-y-2 text-sm text-slate-700">
      <li>Classical atomistic molecular dynamics</li>
      <li>Reactive and empirical force fields (ReaxFF, AIREBO, COMPASS)</li>
      <li>Grand canonical Monte Carlo (fix gcmc) and adsorption workflows</li>
      <li>Polymer chain metrics and transport: R<sub>g</sub>, end-to-end, MSD, diffusivity</li>
      <li>Hydrogen storage analysis: binding-energy distributions, gravimetric/volumetric metrics</li>
      </ul>
  </div>

  <div class="space-y-3 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
    <h3 class="text-xl font-semibold text-brand border-b pb-2">Technical Skills</h3>
    <ul class="mt-3 list-disc list-inside space-y-2 text-sm text-slate-700">
      <li>OS: Linux, macOS, Windows</li>
      <li>Simulation software: LAMMPS, Materials Studio, GROMACS, NAMD</li>
      <li>Visualization &amp; analysis: OVITO, VMD, MDAnalysis, Matplotlib</li>
      <li>Programming: Python (NumPy, pandas), Bash; C++</li>
      <li>ML &amp; potentials: PyTorch, DeepMD-kit, training/validation pipelines</li>
      </ul>
  </div>
</section>


</div>
