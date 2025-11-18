# Personal site

A Jekyll-powered personal research website for Krishna Kumar Patel (PhD student, Chemical Engineering, IIT Delhi). 

## Getting started

### Prerequisites
- Ruby 3.x
- Bundler (`gem install bundler`)

### Install dependencies
```bash
bundle install
```

### Run the site locally
```bash
bundle exec jekyll serve --livereload
```
Then open [http://localhost:4000/crisnapatel](http://localhost:4000/crisnapatel) in your browser.

> If you prefer a zero-dependency static preview, build the site (`bundle exec jekyll build`) and serve the `_site/` directory using `python -m http.server 8000`.

## Deployment

### GitHub Pages
1. Push the `main` branch to GitHub.
2. In the repository settings, enable GitHub Pages with the `GitHub Actions` workflow (default for GitHub Pages + Jekyll) or point Pages to the `main` branch with the `/docs` folder disabled (build output served from the root by GitHub Pages).
3. GitHub Pages will automatically build the Jekyll site using the configuration in `_config.yml`.

### Institute web server (manual upload)
1. Run `bundle exec jekyll build`.
2. Upload the contents of the generated `_site/` directory to your IIT Delhi web space (e.g., via `scp _site/* username@web.iitd.ac.in:public_html/`).
3. Ensure `.nojekyll` is included so the files are served without Jekyll processing on the institute server.

## Repository structure
```
_includes/        Shared head, header, and footer partials
_layouts/         Page templates used by Markdown content
_data/navigation  Single source of truth for navigation links
assets/images/    Portrait, favicon, and other imagery
assets/docs/      CV placeholder (PDF) and downloadable files
assets/scripts/   Convenience and MD-related helper scripts from the legacy site
assets/js/        Client-side enhancements (e.g., contact form submission helper)
pages/            Standalone pages (Research, Publications, CV, Contact)
```

## Contact form integration

### Formspree (default setup)
1. Visit [Formspree](https://formspree.io/) and create a new form to obtain your form ID.
2. In `pages/contact.md`, replace `<YOUR_FORM_ID>` in the `action="https://formspree.io/f/<YOUR_FORM_ID>"` attribute with your actual ID.
3. Deploy the site. When JavaScript is available, `assets/js/contact-form.js` intercepts the submission, posts the form data via `fetch`, and shows an inline confirmation. Without JavaScript the browser falls back to a standard POST request (Formspree will send you a confirmation email).

### FormKeep (alternative service)
1. Create a form in [FormKeep](https://formkeep.com/) and copy the endpoint that looks like `https://formkeep.com/f/xxxxxxxxxxxx`.
2. Update the `action` attribute in `pages/contact.md` to that endpoint. The enhancement script automatically uses whatever URL is configured, so no further changes are required.
3. (Optional) If FormKeep expects additional hidden fields (e.g., `utf8`), add them to the form alongside the provided `_subject` and `_gotcha` inputs.

### Netlify Forms (optional alternative)
1. Remove the Formspree action or set it to an empty string (`action=""`).
2. Add the `data-netlify="true" netlify-honeypot="bot-field"` attributes to the `<form>` tag as noted in the inline comment.
3. Uncomment the hidden `<input type="hidden" name="form-name" value="contact" />` field so Netlify recognises the form at build time.
4. (Optional) Keep the JavaScript enhancement; it automatically stands down when no endpoint is configured, allowing Netlify to handle the submission natively.

Both approaches include an accessible inline success/error state and a mailto fallback (`mailto:{{ site.person.email }}`) for visitors who prefer emailing directly.

## Accessibility & performance
- Semantic HTML structure with accessible navigation and skip links.
- Tailwind CSS via CDN with responsive layout utilities.
- Alt text for images and descriptive link text throughout the site.

## Assumptions & placeholders
- Publications are summarised as work in preparation because the original institute page did not list formal citations.
- The CV PDF is a placeholder noting that the full document will be provided upon request.
- External assets (scripts and descriptions) are carried over from the legacy site and remain shared as-is.

If you update any of these placeholders, remember to revise the corresponding sections on the site and in this README.
