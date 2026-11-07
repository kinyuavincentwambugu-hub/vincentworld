# Vincent's World: deployment folder

Everything in this folder goes online together. `index.html` is your portfolio.
Your address is already set to **https://vincentworld.onrender.com** in `index.html`, `robots.txt` and `sitemap.xml`.

## What is inside
| File | What it does |
|---|---|
| `index.html` | The whole portfolio (design, animations, loading page, all field pages) |
| `preview.jpg` | Picture shown when your link is shared on WhatsApp, LinkedIn, etc. (Open Graph image) |
| `favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `site.webmanifest` | Browser tab icon and phone home-screen icon |
| `robots.txt`, `sitemap.xml` | Tell Google it may read the site and where the map is |
| `RENDER-HEADERS.md` | The security headers to paste into Render (Settings > Headers) |
| `_headers` | The same headers for Netlify or Cloudflare Pages, if you ever move |
| `404.html`, `404.css` | Page shown for a wrong address |
| `nojs.css` | Keeps the page usable for visitors who turn JavaScript off |
| `tools/set-domain.py` | Swaps in a new domain later (for example a .co.ke) |
| `tools/update-csp-hash.py` | Run only if you edit the script or style inside `index.html` |

## Upload to Render (replace the old version)
Your live site is still the old copy. Put these files in place of it:
1. If your Render site deploys from GitHub: copy every file from this folder into the repository (replace the old `index.html`), commit, and Render redeploys. Keep the publish directory pointing at the folder that holds `index.html`.
2. Add the security headers: open `RENDER-HEADERS.md` and enter each one under Settings > Headers on Render. Render ignores the `_headers` file.
3. Open https://vincentworld.onrender.com/robots.txt and https://vincentworld.onrender.com/sitemap.xml to confirm both load.

## Open Graph (share preview)
Already included in `index.html`: title, description, image (`preview.jpg`, 1200 x 630), address, site name, plus Twitter card tags. To test, paste your link into https://www.opengraph.xyz or send it to yourself on WhatsApp. Social apps keep an old preview for a while, so give them time or use each platform's debugger to refresh.

## Google
Follow the Search Console steps from the guide: add `https://vincentworld.onrender.com`, submit `sitemap.xml`, then request indexing of the home page.

## Security: what was done
- Security headers (see `RENDER-HEADERS.md`) and a matching Content-Security-Policy inside `index.html`, which still protects you if the headers are missing. Together they stop other sites framing yours, stop injected scripts and outside connections, and block outside forms.
- No debug mode, no `console.log` and no test code exist in the site.
- No packages or libraries to update. The only outside file is the Google Fonts stylesheet.
- Dead code removed: the old pop-up window, hidden panel code, unused styles and the dog.
- Contact form limits: name 80, email 120, subject 120, message 1,000 characters. Hidden control characters are stripped, `<` and `>` are refused in name and subject, links in a message are capped at 3, and there is a spam trap and a 20-second pause between sends.
- The form opens the visitor's email app. It does not send to a server, so there is no server of yours to attack. Rules in the browser can be bypassed by an expert, so treat them as spam control, not as a lock.

## Security: what only you can do
1. Turn on two-step verification for your Render account, GitHub and the Gmail address shown on the site.
2. Use a different strong password for each account, and never share them.
3. If you buy your own domain later, lock it and turn on auto-renew at the registrar.

## If you edit `index.html` later
Changing the `<script>` or `<style>` changes their fingerprint and the browser will block them. Run `python3 tools/update-csp-hash.py` afterwards, then copy the new policy line from `_headers` into Render. Changing only text outside those two blocks needs nothing.
