---
layout: page
title: Interactive Concepts
permalink: /concepts/
description: "Interactive visualizations of fundamental concepts in molecular dynamics and polymer physics."
subtitle: "Educational tools to understand complex scientific ideas"
---

A collection of interactive web-based explanations for key concepts in molecular dynamics, polymer physics, and computational materials science. These visualizations were created to make abstract scientific ideas more intuitive and accessible.

## Available Visualizations

<div class="grid gap-6 md:grid-cols-2">
  <article class="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-sm hover:shadow-md transition">
    <h3 class="text-lg font-semibold text-brand">
      <a href="{{ '/assets/concepts/MSD_Calculation.html' | relative_url }}" class="hover:underline">
        Einstein Mean Square Displacement (MSD) Analysis
      </a>
    </h3>
    <p class="mt-2 text-sm text-slate-700">
      Interactive tutorial on calculating diffusion coefficients from molecular dynamics trajectories. Learn about center-of-mass calculations, unwrapping periodic boundary conditions, the sliding window algorithm, and linear fitting techniques to extract transport properties from polymer chain motion.
    </p>
    <p class="mt-3 text-xs text-slate-500 italic">
      Demonstration using LAMMPS trajectory data with real-time MSD calculation and visualization
    </p>
  </article>

  <article class="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-sm hover:shadow-md transition">
    <h3 class="text-lg font-semibold text-brand">
      <a href="{{ '/assets/concepts/OACF.html' | relative_url }}" class="hover:underline">
        Orientational Autocorrelation Function (OACF)
      </a>
    </h3>
    <p class="mt-2 text-sm text-slate-700">
      Understanding how molecular segments relax and rotate over time. Explore the geometry of vector definitions, Legendre polynomials, time evolution of correlation functions, and how to interpret relaxation time ratios to distinguish between diffusional and jump-like motion.
    </p>
    <p class="mt-3 text-xs text-slate-500 italic">
      Based on: Horinaka et al., "Molecular dynamics simulation of local motion of polystyrene chain end—comparison with the fluorescence depolarization study"
    </p>
  </article>
</div>

---

## Educational Resources

<div class="grid gap-6 md:grid-cols-2">
  <article class="rounded-2xl border border-slate-200 bg-white/70 p-6 shadow-sm hover:shadow-md transition">
    <h3 class="text-lg font-semibold text-brand">
      <a href="https://crisnapatel.github.io/python-basics/" class="hover:underline">
        Computational Techniques — Python Basics
      </a>
    </h3>
    <p class="mt-2 text-sm text-slate-700">
      A practical guide for CHL7002 students at IIT Delhi. Learn Python fundamentals including variables, data types, control flow, functions, NumPy, Pandas, and how to read and fix common errors.
    </p>
    <p class="mt-3 text-xs text-slate-500 italic">
      Course: CHL7002 Computational Techniques for Chemical Engineers
    </p>
  </article>
</div>

---

More concepts coming soon...
