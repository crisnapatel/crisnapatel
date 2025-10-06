(function () {
  document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const okEl = document.getElementById('contact-success');
    const errEl = document.getElementById('contact-error');
    const btn = form.querySelector('button[type="submit"]');
    const fallbackEmail = form.dataset.fallbackEmail || 'chz218339@iitd.ac.in';

    // Must be a valid Formspree endpoint like: https://formspree.io/f/xxxxabcd
    const action = form.getAttribute('action') || '';
    if (!/https:\/\/formspree\.io\/f\/[A-Za-z0-9]+/.test(action)) return;

    function show(el, msg) {
      if (!el) return;
      if (msg) el.innerHTML = msg;
      el.classList.remove('hidden');
      if (typeof el.focus === 'function') el.focus({ preventScroll: false });
    }
    function hide(el) { if (el) el.classList.add('hidden'); }

    form.addEventListener('submit', async function (e) {
      // block bots
      const honeypot = form.querySelector('input[name="_gotcha"]');
      if (honeypot && honeypot.value) { e.preventDefault(); return; }

      if (typeof form.reportValidity === 'function' && !form.reportValidity()) {
        e.preventDefault(); return;
      }
      e.preventDefault();

      hide(okEl); hide(errEl);
      if (btn) { btn.dataset.t = btn.textContent; btn.textContent = 'Sending…'; btn.disabled = true; btn.setAttribute('aria-busy','true'); }

      const fd = new FormData(form);

      try {
        const res = await fetch(action, {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body: fd
        });

        if (res.ok) {
          form.reset();
          show(okEl);
        } else {
          let msg = 'There was a problem sending your message.';
          try {
            const data = await res.json();
            if (data && data.errors && Array.isArray(data.errors)) {
              msg = data.errors.map(e => e.message).join('<br>');
            } else if (data && data.error) {
              msg = data.error;
            }
          } catch {}
          msg += ` <a class="font-semibold text-accent hover:underline" href="mailto:${encodeURIComponent(fallbackEmail)}?subject=Website%20message%20fallback">Email me</a>.`;
          show(errEl, msg);
        }
      } catch {
        const msg = `Network error. Please try again or <a class="font-semibold text-accent hover:underline" href="mailto:${encodeURIComponent(fallbackEmail)}?subject=Website%20message%20fallback">email me directly</a>.`;
        show(errEl, msg);
      } finally {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t || 'Submit'; btn.removeAttribute('aria-busy'); }
      }
    });
  });
})();
