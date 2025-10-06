(function () {
  document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const successMessage = document.getElementById('contact-success');
    const errorMessage = document.getElementById('contact-error');
    const submitButton = form.querySelector('button[type="submit"]');
    const fallbackEmail = form.dataset.fallbackEmail || 'chz218339@iitd.ac.in';
    const isFormspree = (form.getAttribute('action') || '').includes('formspree.io');

    if (!isFormspree) {
      return;
    }

    function showMessage(element) {
      if (!element) return;
      element.classList.remove('hidden');
      if (typeof element.focus === 'function') {
        element.focus({ preventScroll: false });
      }
    }

    function hideMessage(element) {
      if (!element) return;
      element.classList.add('hidden');
    }

    form.addEventListener('submit', async function (event) {
      if (typeof form.reportValidity === 'function' && !form.reportValidity()) {
        event.preventDefault();
        return;
      }

      event.preventDefault();

      hideMessage(successMessage);
      hideMessage(errorMessage);

      if (submitButton) {
        submitButton.dataset.originalText = submitButton.dataset.originalText || submitButton.textContent;
        submitButton.textContent = 'Sending…';
        submitButton.disabled = true;
      }

      const formData = new FormData(form);

      try {
        const response = await fetch(form.action, {
          method: form.method || 'POST',
          headers: {
            Accept: 'application/json',
          },
          body: formData,
        });

        if (response.ok) {
          form.reset();
          showMessage(successMessage);
          return;
        }

        let errorText = 'There was a problem sending your message. You can email me directly instead.';
        try {
          const data = await response.json();
          if (data && data.error) {
            errorText = data.error;
          }
        } catch (jsonError) {
          // ignore JSON parsing errors
        }

        if (errorMessage) {
          errorMessage.innerHTML = `${errorText} <a class="font-semibold text-accent hover:underline" href="mailto:${encodeURIComponent(fallbackEmail)}?subject=Website%20message%20fallback">Email me</a>.`;
          showMessage(errorMessage);
        }
      } catch (networkError) {
        if (errorMessage) {
          errorMessage.innerHTML = `Network error. Please try again or <a class="font-semibold text-accent hover:underline" href="mailto:${encodeURIComponent(fallbackEmail)}?subject=Website%20message%20fallback">email me directly</a>.`;
          showMessage(errorMessage);
        }
      } finally {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.textContent = submitButton.dataset.originalText || 'Submit';
        }
      }
    });
  });
})();
