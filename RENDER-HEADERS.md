# Security headers for Render

Render does not read the `_headers` file. Add these in the Render dashboard instead:
open your site, then **Settings > Headers**, and add each row below with the path `/*`.
Names are not case sensitive. Paste each value exactly as shown.

**Name:** `Content-Security-Policy`

**Value:**

```
default-src 'none'; script-src 'sha256-9AV1b+o+zr/Xv1eEcKkuKPXAGyQCFRlNJUFQ8BkGRyI='; style-src 'self' 'sha256-YUqiMRbJSMEhfcj3L7xVBIib0bwPSFZFk2d38ggwp34=' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; manifest-src 'self'; connect-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none'; upgrade-insecure-requests; frame-ancestors 'none'
```

**Name:** `X-Content-Type-Options`

**Value:**

```
nosniff
```

**Name:** `X-Frame-Options`

**Value:**

```
DENY
```

**Name:** `Referrer-Policy`

**Value:**

```
strict-origin-when-cross-origin
```

**Name:** `Permissions-Policy`

**Value:**

```
accelerometer=(), camera=(), geolocation=(), gyroscope=(), microphone=(), payment=(), usb=()
```

**Name:** `Cross-Origin-Opener-Policy`

**Value:**

```
same-origin
```

**Name:** `Strict-Transport-Security`

**Value:**

```
max-age=31536000
```

**Name:** `X-Permitted-Cross-Domain-Policies`

**Value:**

```
none
```

After saving, redeploy. Then check your site at https://securityheaders.com.

Important: if you ever edit the `<script>` or `<style>` inside `index.html`, run `python3 tools/update-csp-hash.py`, then copy the new Content-Security-Policy value from `_headers` into Render, otherwise the browser blocks your page's script.
