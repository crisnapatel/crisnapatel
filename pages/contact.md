---
layout: page
title: Contact
permalink: /contact/
description: "Contact Krishna Patel for collaborations, student mentorship, or molecular simulation discussions."
meta:
  title: "Contact Krishna Patel — Molecular simulations and collaborations"
  description: "Send a message to Krishna Patel about research in molecular dynamics, hydrogen storage, or teaching."
---

<div class="not-prose space-y-12">
  <div class="grid gap-10 md:grid-cols-2">
    <div class="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
      <h1 class="text-2xl font-semibold text-brand">Send a message</h1>
      <p class="mt-2 text-sm text-slate-600">
        I respond to most messages within two working days. Share your research context and any specific questions so I can prepare resources in advance.
      </p>
      <!-- To enable hosted forms, replace the action with your Formspree endpoint or leave it blank for Netlify processing.
           Remove the data-demo attribute once a backend is configured. -->
      <form
        id="contact-form"
        name="contact"
        method="POST"
        action="mailto:chz218339@iitd.ac.in"
        enctype="text/plain"
        data-netlify="true"
        data-demo="true"
        class="mt-6 space-y-5"
      >
        <input type="hidden" name="form-name" value="contact" />
        <div>
          <label class="block text-sm font-semibold text-brand" for="contact-name">Name</label>
          <input
            id="contact-name"
            name="name"
            type="text"
            required
            autocomplete="name"
            class="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 text-slate-800 shadow-sm focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/40"
          />
        </div>
        <div>
          <label class="block text-sm font-semibold text-brand" for="contact-email">Email</label>
          <input
            id="contact-email"
            name="email"
            type="email"
            required
            autocomplete="email"
            pattern="^[^@\s]+@[^@\s]+\.[^@\s]+$"
            class="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 text-slate-800 shadow-sm focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/40"
          />
        </div>
        <div>
          <label class="block text-sm font-semibold text-brand" for="contact-message">Message</label>
          <textarea
            id="contact-message"
            name="message"
            rows="5"
            required
            class="mt-2 w-full rounded-xl border border-slate-300 px-4 py-3 text-slate-800 shadow-sm focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/40"
          ></textarea>
        </div>
        <button
          type="submit"
          class="inline-flex items-center gap-2 rounded-full bg-brand px-6 py-3 text-sm font-semibold text-white shadow focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2"
          aria-label="Send contact message to Krishna Patel"
        >
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 8.25l8.955 4.477a2.25 2.25 0 001.99 0L22 8.25M4.5 19.5h15a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5h-15A1.5 1.5 0 003 6v12a1.5 1.5 0 001.5 1.5z" />
          </svg>
          Submit
        </button>
        <p id="contact-success" class="hidden rounded-xl bg-emerald-50 px-4 py-3 text-sm text-emerald-700" role="status">
          Thank you for reaching out! Your message was noted—I'll reply soon.
        </p>
      </form>
      <p class="mt-4 text-sm text-slate-600">
        Prefer direct email? Write to <a class="font-semibold text-accent hover:underline" href="mailto:chz218339@iitd.ac.in">chz218339@iitd.ac.in</a>.
      </p>
    </div>
    <div class="space-y-6">
      <div class="rounded-3xl border border-slate-200 bg-white p-6 text-center shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-accent/10 text-accent">
          <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 21c4.97-4.97 9-8.25 9-12a9 9 0 10-18 0c0 3.75 4.03 7.03 9 12z" />
          </svg>
        </div>
        <h2 class="mt-4 text-lg font-semibold text-brand">Visit Us</h2>
        <p class="mt-2 text-sm leading-relaxed text-slate-600">
          Department of Chemical Engineering<br />
          Indian Institute of Technology Delhi<br />
          Hauz Khas, New Delhi - 110016
        </p>
      </div>
      <div class="rounded-3xl border border-slate-200 bg-white p-6 text-center shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-accent/10 text-accent">
          <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 8.25l8.955 4.477a2.25 2.25 0 001.99 0L22 8.25M4.5 19.5h15a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5h-15A1.5 1.5 0 003 6v12a1.5 1.5 0 001.5 1.5z" />
          </svg>
        </div>
        <h2 class="mt-4 text-lg font-semibold text-brand">Email</h2>
        <p class="mt-2 text-sm text-slate-600">chz218339@iitd.ac.in</p>
      </div>
      <div class="rounded-3xl border border-slate-200 bg-white p-6 text-center shadow-sm">
        <div class="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-accent/10 text-accent">
          <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 5.25a.75.75 0 01.75-.75h3.5a.75.75 0 01.75.75v2.25a.75.75 0 01-.75.75H4.5v8.25A1.5 1.5 0 006 18h3a1.5 1.5 0 001.5-1.5V8.25h-.75a.75.75 0 01-.75-.75V5.25a.75.75 0 01.75-.75H12a.75.75 0 01.75.75v12.75a2.25 2.25 0 01-2.25 2.25H6a2.25 2.25 0 01-2.25-2.25V9H3a.75.75 0 01-.75-.75V5.25z" />
          </svg>
        </div>
        <h2 class="mt-4 text-lg font-semibold text-brand">Phone</h2>
        <p class="mt-2 text-sm text-slate-600">+91 7389506644</p>
      </div>
    </div>
  </div>

  <section class="rounded-3xl border border-slate-200 bg-white p-8 text-center shadow-sm">
    <h2 class="text-xl font-semibold text-brand">Connect with Me</h2>
    <p class="mt-2 text-sm text-slate-600">Follow research updates and resource drops on these platforms.</p>
    <div class="mt-6 flex flex-wrap items-center justify-center gap-4">
      {% assign linkedin = site.social.linkedin | default: '<<add linkedin>>' %}
      {% if linkedin contains '<<add' %}
        <span class="flex items-center gap-2 rounded-full border border-dashed border-slate-300 px-4 py-2 text-sm text-slate-500">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M20.447 20.452H16.89v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.94v5.666H9.345V9h3.409v1.561h.049c.475-.9 1.637-1.852 3.366-1.852 3.598 0 4.266 2.368 4.266 5.451v6.292zM5.337 7.433a1.982 1.982 0 110-3.964 1.982 1.982 0 010 3.964zM7.119 20.452H3.554V9h3.565v11.452z" />
          </svg>
          LinkedIn — <<add profile>>
        </span>
      {% else %}
        <a class="flex h-12 w-12 items-center justify-center rounded-full bg-accent text-white transition hover:bg-brand focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ linkedin }}" target="_blank" rel="noopener" aria-label="LinkedIn">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M20.447 20.452H16.89v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.94v5.666H9.345V9h3.409v1.561h.049c.475-.9 1.637-1.852 3.366-1.852 3.598 0 4.266 2.368 4.266 5.451v6.292zM5.337 7.433a1.982 1.982 0 110-3.964 1.982 1.982 0 010 3.964zM7.119 20.452H3.554V9h3.565v11.452z" />
          </svg>
        </a>
      {% endif %}

      {% assign twitter = site.social.twitter | default: '<<add twitter>>' %}
      {% if twitter contains '<<add' %}
        <span class="flex items-center gap-2 rounded-full border border-dashed border-slate-300 px-4 py-2 text-sm text-slate-500">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M19.633 7.997c.013.176.013.352.013.528 0 5.381-4.095 11.578-11.578 11.578-2.301 0-4.435-.676-6.231-1.848.319.037.626.05.957.05a8.18 8.18 0 005.067-1.741 4.089 4.089 0 01-3.817-2.836c.254.037.508.063.775.063.37 0 .74-.05 1.085-.139a4.081 4.081 0 01-3.273-4.003v-.05c.546.303 1.175.482 1.843.508A4.076 4.076 0 012.8 6.081a11.585 11.585 0 008.41 4.267 4.605 4.605 0 01-.101-.935 4.087 4.087 0 017.066-2.79 8.045 8.045 0 002.593-.987 4.087 4.087 0 01-1.796 2.257 8.166 8.166 0 002.357-.632 8.78 8.78 0 01-2.596 2.056z" />
          </svg>
          Twitter — <<add handle>>
        </span>
      {% else %}
        <a class="flex h-12 w-12 items-center justify-center rounded-full bg-accent text-white transition hover:bg-brand focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ twitter }}" target="_blank" rel="noopener" aria-label="Twitter">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M19.633 7.997c.013.176.013.352.013.528 0 5.381-4.095 11.578-11.578 11.578-2.301 0-4.435-.676-6.231-1.848.319.037.626.05.957.05a8.18 8.18 0 005.067-1.741 4.089 4.089 0 01-3.817-2.836c.254.037.508.063.775.063.37 0 .74-.05 1.085-.139a4.081 4.081 0 01-3.273-4.003v-.05c.546.303 1.175.482 1.843.508A4.076 4.076 0 012.8 6.081a11.585 11.585 0 008.41 4.267 4.605 4.605 0 01-.101-.935 4.087 4.087 0 017.066-2.79 8.045 8.045 0 002.593-.987 4.087 4.087 0 01-1.796 2.257 8.166 8.166 0 002.357-.632 8.78 8.78 0 01-2.596 2.056z" />
          </svg>
        </a>
      {% endif %}

      {% assign github = site.social.github | default: '<<add github>>' %}
      {% if github contains '<<add' %}
        <span class="flex items-center gap-2 rounded-full border border-dashed border-slate-300 px-4 py-2 text-sm text-slate-500">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path fill-rule="evenodd" d="M12 .5C5.648.5.5 5.648.5 12c0 5.084 3.292 9.387 7.865 10.912.575.1.786-.25.786-.555 0-.274-.01-1.18-.015-2.142-3.2.696-3.877-1.542-3.877-1.542-.523-1.328-1.277-1.682-1.277-1.682-1.044-.714.079-.7.079-.7 1.155.081 1.763 1.187 1.763 1.187 1.027 1.761 2.695 1.253 3.353.958.104-.744.402-1.253.732-1.541-2.553-.291-5.237-1.276-5.237-5.68 0-1.255.45-2.28 1.186-3.084-.119-.29-.514-1.46.112-3.044 0 0 .966-.309 3.167 1.178a11.02 11.02 0 012.883-.388c.978.004 1.963.132 2.883.388 2.2-1.487 3.165-1.178 3.165-1.178.627 1.584.232 2.754.114 3.044.739.804 1.185 1.829 1.185 3.084 0 4.417-2.689 5.385-5.252 5.671.414.355.78 1.052.78 2.123 0 1.533-.014 2.77-.014 3.147 0 .308.208.66.791.548C20.713 21.382 24 17.082 24 12 24 5.648 18.352.5 12 .5z" clip-rule="evenodd" />
          </svg>
          GitHub — <<add profile>>
        </span>
      {% else %}
        <a class="flex h-12 w-12 items-center justify-center rounded-full bg-accent text-white transition hover:bg-brand focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ github }}" target="_blank" rel="noopener" aria-label="GitHub">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path fill-rule="evenodd" d="M12 .5C5.648.5.5 5.648.5 12c0 5.084 3.292 9.387 7.865 10.912.575.1.786-.25.786-.555 0-.274-.01-1.18-.015-2.142-3.2.696-3.877-1.542-3.877-1.542-.523-1.328-1.277-1.682-1.277-1.682-1.044-.714.079-.7.079-.7 1.155.081 1.763 1.187 1.763 1.187 1.027 1.761 2.695 1.253 3.353.958.104-.744.402-1.253.732-1.541-2.553-.291-5.237-1.276-5.237-5.68 0-1.255.45-2.28 1.186-3.084-.119-.29-.514-1.46.112-3.044 0 0 .966-.309 3.167 1.178a11.02 11.02 0 012.883-.388c.978.004 1.963.132 2.883.388 2.2-1.487 3.165-1.178 3.165-1.178.627 1.584.232 2.754.114 3.044.739.804 1.185 1.829 1.185 3.084 0 4.417-2.689 5.385-5.252 5.671.414.355.78 1.052.78 2.123 0 1.533-.014 2.77-.014 3.147 0 .308.208.66.791.548C20.713 21.382 24 17.082 24 12 24 5.648 18.352.5 12 .5z" clip-rule="evenodd" />
          </svg>
        </a>
      {% endif %}

      {% assign scholar = site.social.google_scholar | default: '<<add google scholar>>' %}
      {% if scholar contains '<<add' %}
        <span class="flex items-center gap-2 rounded-full border border-dashed border-slate-300 px-4 py-2 text-sm text-slate-500">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2L1 8l11 6 9-4.91V17h2V8L12 2zm0 7.37l-6.46-3.53L12 3.94l6.46 3.9L12 9.37zM12 14l-4.37-2.38L12 9.87l4.37 1.75L12 14zm0 2.5a4.5 4.5 0 100 9 4.5 4.5 0 000-9zm0 6.5a2 2 0 110-4 2 2 0 010 4z" />
          </svg>
          Google Scholar — <<add profile>>
        </span>
      {% else %}
        <a class="flex h-12 w-12 items-center justify-center rounded-full bg-accent text-white transition hover:bg-brand focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ scholar }}" target="_blank" rel="noopener" aria-label="Google Scholar">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2L1 8l11 6 9-4.91V17h2V8L12 2zm0 7.37l-6.46-3.53L12 3.94l6.46 3.9L12 9.37zM12 14l-4.37-2.38L12 9.87l4.37 1.75L12 14zm0 2.5a4.5 4.5 0 100 9 4.5 4.5 0 000-9zm0 6.5a2 2 0 110-4 2 2 0 010 4z" />
          </svg>
        </a>
      {% endif %}

      {% assign orcid = site.social.orcid | default: '<<add orcid>>' %}
      {% if orcid contains '<<add' %}
        <span class="flex items-center gap-2 rounded-full border border-dashed border-slate-300 px-4 py-2 text-sm text-slate-500">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 1.75a10.25 10.25 0 110 20.5 10.25 10.25 0 010-20.5zM9.5 7.75H8v8.5h1.5v-8.5zm2.87 0h-1.47v8.5h2.8c2.26 0 3.6-1.4 3.6-4.23 0-2.67-1.47-4.27-3.96-4.27h-.97zm0 7.24v-6h1.02c1.6 0 2.37 1.02 2.37 2.97 0 1.87-.86 3.03-2.37 3.03h-1.02z" />
          </svg>
          ORCID — <<add iD>>
        </span>
      {% else %}
        <a class="flex h-12 w-12 items-center justify-center rounded-full bg-accent text-white transition hover:bg-brand focus:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2" href="{{ orcid }}" target="_blank" rel="noopener" aria-label="ORCID">
          <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 1.75a10.25 10.25 0 110 20.5 10.25 10.25 0 010-20.5zM9.5 7.75H8v8.5h1.5v-8.5zm2.87 0h-1.47v8.5h2.8c2.26 0 3.6-1.4 3.6-4.23 0-2.67-1.47-4.27-3.96-4.27h-.97zm0 7.24v-6h1.02c1.6 0 2.37 1.02 2.37 2.97 0 1.87-.86 3.03-2.37 3.03h-1.02z" />
          </svg>
        </a>
      {% endif %}
    </div>
  </section>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    const success = document.getElementById('contact-success');
    if (!form || !success) return;

    form.addEventListener('submit', function (event) {
      if (!form.reportValidity()) {
        event.preventDefault();
        return;
      }

      if (form.dataset.demo === 'true') {
        event.preventDefault();
        form.reset();
        success.classList.remove('hidden');
        success.focus?.();
      }
    });
  });
</script>
