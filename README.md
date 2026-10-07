# Ascend site

The founding-member landing page for Ascend, a strength coaching app. Static HTML plus one Vercel function.

- `index.html` is generated. Edit `build/landing.py` (copy and layout) and run `python3 build/landing.py`. Do not edit the HTML by hand.
- `build/*.py` other than `landing.py` are a copy of the app's design-v5 mockup builder (`ascend/design-v5/build`); the phones on the page are the app's own frames. When the app's frames change, copy those files over and rebuild.
- `preview/ascend-landing.html` is the same page without the document skeleton, for publishing as a Claude artifact.
- `api/apply.js` receives the application form and emails it through Resend.
- Icons (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `icon-*.png`), `og.png` (link preview), `robots.txt`, `sitemap.xml`, `site.webmanifest`. The site URL is set once as `SITE` in `build/landing.py` and repeated in `robots.txt` / `sitemap.xml`; change all three when the domain changes.

## Deploy (Vercel)
```
npx vercel            # first time: new project, no build command, output directory "."
npx vercel env add RESEND_API_KEY production
npx vercel env add APPLY_TO production        # your inbox
npx vercel env add APPLY_FROM production      # Ascend <onboarding@resend.dev>  until the domain is verified in Resend
npx vercel --prod
```
Domain: Vercel → Project → Settings → Domains → add; at the registrar, A `@` → 76.76.21.21, CNAME `www` → cname.vercel-dns.com.

## Before sharing the link
- Replace `hello@ascend.coach` (two places in `build/landing.py`) and set the places meter honestly (`i < 3`, "3 of 20 taken").
- Footer links Terms · Privacy · Contact point nowhere yet.
- Resend's default sender delivers only to the account's own email; verify the domain in Resend → Domains and set `APPLY_FROM` to `Ascend <apply@yourdomain>` once you have it.
