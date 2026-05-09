# MsGamer — Claude Code Context

## Project overview

**Problem:** Paulina Lorné's personal site (msgamer.se) is outdated and doesn't reflect her seniority as Nordic Marketing Manager at Bethesda.
**For whom:** Recruiters, industry peers, potential collaborators in the gaming industry.
**Success looks like:** A modern, professional portfolio that leads with her career achievements while keeping the pink identity and gaming personality that make her memorable.

## Tech stack

| Layer | Choice | Why |
|-------|--------|-----|
| Build | Vite | Fast dev server, asset optimization, multi-page support |
| Styling | Vanilla CSS + custom properties | Design system is specific — utilities add noise. |
| JavaScript | Vanilla ES modules | Minimal JS needed (scroll animations, marquee, mobile nav) |
| Fonts | Clash Display + General Sans (FontShare) | Editorial personality with clean body text |
| Deployment | Static files on Loopia (FTP/SFTP) | WordPress was retired; we drop `dist/` contents into `public_html` |

## Design system

See `docs/superpowers/specs/2026-03-30-msgamer-redesign-design.md` for full spec.

**Colors:** Hot Pink `#e84da0`, Blush `#fef7fa`, White `#ffffff`, Ink `#1a1a2e`, Slate `#6b7280`, Pink Border `#fce4ef`
**Fonts:** Clash Display (headings), General Sans (body)
**One pink rule:** Use `#e84da0` consistently. No gradient mixing.

## Commands

- `npm run dev` — Start Vite dev server
- `npm run build` — Build to `dist/`
- `npm run preview` — Preview production build

## Deploy

Live host: Loopia (Apache 2.4 + mpm-itk on FreeBSD, nginx fronting). Live URL: https://msgamer.se.

1. `npm run build` — produces `dist/` (~388 KB, 17 files)
2. Upload **everything in `dist/` including the hidden `.htaccess`** to Loopia's `public_html`. In FileZilla/Cyberduck: enable "Show hidden files" so `.htaccess` is visible.
3. Force-HTTPS is enabled in **Loopia's kundzon**, not in `.htaccess` (see gotchas below).

## Asset paths

- `images/paulina.jpg`, `images/logo.png`, `images/favicon.svg`, `images/apple-touch-icon.png` — referenced via `<img src>` or `<link href>`. Vite hashes them into `dist/assets/`.
- `public/images/og-image.jpg` — referenced via `<meta property="og:image">` with absolute URL. Vite does NOT process meta-tag URLs, so this MUST live in `public/images/` to be copied verbatim to `dist/images/og-image.jpg`.

## Loopia .htaccess gotchas

These trigger 500 Internal Server Error on Loopia even when wrapped in `<IfModule>` guards. Don't add them back.

- **`Options -Indexes`** — Loopia disallows the `Options` directive in `.htaccess`.
- **`AddOutputFilterByType DEFLATE …`** — Loopia rejects user-level mod_deflate config. They compress server-level (verified: `content-encoding: gzip` arrives without our directive).
- **`RewriteCond %{HTTPS} !=on` + redirect to `https://`** — `%{HTTPS}` reports `off` even on HTTPS requests because of Loopia's frontend proxy. The redirect loops. Force HTTPS in kundzon instead.

What works on Loopia and is in our `public/.htaccess`: `ErrorDocument`, `DirectoryIndex`, `Header set/always set`, `Cache-Control` via `<FilesMatch>`, `RewriteRule` for clean URLs and www→non-www.

Apache error log is not exposed in Loopia's kundzon. To diagnose a new 500, bisect `.htaccess` or email support@loopia.se.

## Architecture rules

1. Vanilla HTML/CSS/JS only — no frameworks, no build-time templating
2. CSS custom properties for all design tokens — change once, apply everywhere
3. Mobile-first CSS — base styles for mobile, media queries for larger screens
4. Semantic HTML — proper heading hierarchy, landmarks, ARIA where needed
5. All animations respect `prefers-reduced-motion`

## What NOT to do

- Don't add a CSS framework (Tailwind, Bootstrap) — the design system is custom
- Don't add a JS framework (React, Vue) — 5 static pages don't need one
- Don't use fixed pixel font sizes for body text — always rem
- Don't skip alt text on images
- Don't use divs where semantic elements exist (nav, main, section, article, footer)
- Don't link with `.html` suffix (`/about.html`) — use clean URLs (`/about`); the `.htaccess` rewrites map them to the actual files
- Don't add the `.htaccess` directives listed in "Loopia gotchas" above — they take the live site down
