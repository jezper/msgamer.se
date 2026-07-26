# MsGamer Website Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 5-page static portfolio site for Paulina Lorné (MsGamer) — pink-forward, professional, editorial design with micro-animations and full SEO.

**Architecture:** Static site built with Vite + vanilla HTML/CSS/JS. No framework — 5 pages don't need one, and vanilla markup converts cleanly to a WordPress theme later. CSS custom properties for the design system. Intersection Observer for scroll animations. Mobile-first responsive.

**Tech Stack:**
- Build tool: Vite (dev server, asset optimization, font preloading)
- Styling: Vanilla CSS with custom properties (no Tailwind — the design system is specific enough that utility classes add noise)
- JavaScript: Vanilla ES modules (Intersection Observer for scroll animations, marquee for portfolio strip)
- Fonts: Clash Display + General Sans from FontShare
- Images: WebP with fallback
- Testing: Manual browser testing + Lighthouse audits (no unit tests for a static site)

**Design spec:** `docs/superpowers/specs/2026-03-30-msgamer-redesign-design.md`

---

## File Structure

```
/
├── index.html                     # Homepage
├── about.html                     # About + Gaming Roots
├── career.html                    # Featured role + timeline
├── press.html                     # Featured In grid
├── contact.html                   # Contact info
├── css/
│   ├── reset.css                  # Minimal CSS reset
│   ├── tokens.css                 # Design tokens (colors, fonts, spacing)
│   ├── base.css                   # Base element styles (body, headings, links)
│   ├── layout.css                 # Nav, footer, section containers, grid
│   ├── components.css             # Buttons, cards, timeline, portfolio strip
│   └── animations.css             # Scroll animations, hover effects, marquee
├── js/
│   ├── main.js                    # Entry point — imports and initializes modules
│   ├── scroll-animations.js       # Intersection Observer for fade-in/slide-up
│   ├── marquee.js                 # Portfolio strip continuous scroll
│   └── mobile-nav.js              # Hamburger menu toggle
├── images/
│   ├── logo.png                   # Original MsGamer logo
│   ├── paulina-placeholder.gif    # Current photo (placeholder)
│   └── og-image.png               # Open Graph preview image (to be created)
├── package.json                   # Vite dev dependency
├── vite.config.js                 # Vite config (multi-page, asset handling)
├── CLAUDE.md                      # Project context for Claude Code
├── .gitignore                     # Node modules, dist, .superpowers
└── docs/                          # Specs and plans (already exists)
```

**Why this structure:**
- One CSS file per concern — easy to find, easy to modify, easy to extract into WordPress later
- JS modules are tiny and focused — each does one thing
- No `src/` directory — static sites don't need a source/dist separation during development (Vite handles the build)
- Images at root level — simplest path references, maps directly to WordPress theme structure

---

### Task 1: Project Scaffold + Vite Setup

**Files:**
- Create: `package.json`
- Create: `vite.config.js`
- Create: `.gitignore`
- Create: `CLAUDE.md`

- [ ] **Step 1: Initialize git repository**

```bash
cd /Users/jezper.lorne/Projects/Code/MsGamer
git init
```

- [ ] **Step 2: Create package.json**

Create `package.json`:

```json
{
  "name": "msgamer",
  "version": "1.0.0",
  "private": true,
  "description": "Portfolio site for Paulina Lorné — MsGamer",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "vite": "^6.0.0"
  }
}
```

- [ ] **Step 3: Create vite.config.js**

Create `vite.config.js`:

```js
import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        career: resolve(__dirname, 'career.html'),
        press: resolve(__dirname, 'press.html'),
        contact: resolve(__dirname, 'contact.html'),
      },
    },
  },
})
```

- [ ] **Step 4: Create .gitignore**

Create `.gitignore`:

```
node_modules/
dist/
.superpowers/
.DS_Store
```

- [ ] **Step 5: Create CLAUDE.md**

Create `CLAUDE.md`:

```markdown
# MsGamer — Claude Code Context

## Project overview

**Problem:** Paulina Lorné's personal site (msgamer.se) is outdated and doesn't reflect her seniority as Nordic Marketing Manager at Bethesda.
**For whom:** Recruiters, industry peers, potential collaborators in the gaming industry.
**Success looks like:** A modern, professional portfolio that leads with her career achievements while keeping the pink identity and gaming personality that make her memorable.

## Tech stack

| Layer | Choice | Why |
|-------|--------|-----|
| Build | Vite | Fast dev server, asset optimization, multi-page support |
| Styling | Vanilla CSS + custom properties | Design system is specific — utilities add noise. Clean for WordPress conversion. |
| JavaScript | Vanilla ES modules | Minimal JS needed (scroll animations, marquee, mobile nav) |
| Fonts | Clash Display + General Sans (FontShare) | Editorial personality with clean body text |
| Deployment | Static files (Phase 1), WordPress (Phase 2) | Start static, convert to WP theme later |

## Design system

See `docs/superpowers/specs/2026-03-30-msgamer-redesign-design.md` for full spec.

**Colors:** Hot Pink `#e84da0`, Blush `#fef7fa`, White `#ffffff`, Ink `#1a1a2e`, Slate `#6b7280`, Pink Border `#fce4ef`
**Fonts:** Clash Display (headings), General Sans (body)
**One pink rule:** Use `#e84da0` consistently. No gradient mixing.

## Commands

- `npm run dev` — Start Vite dev server
- `npm run build` — Build to `dist/`
- `npm run preview` — Preview production build

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
```

- [ ] **Step 6: Install dependencies**

```bash
npm install
```

- [ ] **Step 7: Commit scaffold**

```bash
git add package.json vite.config.js .gitignore CLAUDE.md
git commit -m "chore: scaffold project with Vite"
```

---

### Task 2: Design Tokens + CSS Foundation

**Files:**
- Create: `css/reset.css`
- Create: `css/tokens.css`
- Create: `css/base.css`

- [ ] **Step 1: Create CSS reset**

Create `css/reset.css`:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  -webkit-text-size-adjust: 100%;
  -moz-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

body {
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}

input,
button,
textarea,
select {
  font: inherit;
}

p,
h1,
h2,
h3,
h4,
h5,
h6 {
  overflow-wrap: break-word;
}

a {
  color: inherit;
  text-decoration: none;
}

ul,
ol {
  list-style: none;
}
```

- [ ] **Step 2: Create design tokens**

Create `css/tokens.css`:

```css
:root {
  /* Colors */
  --color-pink: #e84da0;
  --color-pink-hover: #d63384;
  --color-blush: #fef7fa;
  --color-white: #ffffff;
  --color-ink: #1a1a2e;
  --color-slate: #6b7280;
  --color-pink-border: #fce4ef;
  --color-pink-shadow: rgba(232, 77, 160, 0.08);

  /* Typography — sizes in rem (base 16px) */
  --font-display: 'Clash Display', system-ui, sans-serif;
  --font-body: 'General Sans', system-ui, sans-serif;

  --text-hero: clamp(2.5rem, 5vw, 3.5rem);
  --text-section: clamp(1.75rem, 3vw, 2rem);
  --text-sub: clamp(1.125rem, 2vw, 1.25rem);
  --text-body: clamp(0.9375rem, 1.5vw, 1.0625rem);
  --text-small: 0.8125rem;
  --text-label: 0.6875rem;

  --leading-tight: 1.0;
  --leading-snug: 1.15;
  --leading-normal: 1.7;

  --tracking-tight: -0.094rem;
  --tracking-normal: 0;
  --tracking-wide: 0.0625rem;
  --tracking-wider: 0.125rem;
  --tracking-widest: 0.25rem;

  /* Spacing scale */
  --space-xs: 0.5rem;
  --space-sm: 0.75rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
  --space-3xl: 3.75rem;
  --space-4xl: 4.5rem;

  /* Layout */
  --container-max: 72rem;
  --container-padding: 2.5rem;

  /* Borders */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-normal: 200ms ease;
  --transition-slow: 400ms ease;

  /* Shadows */
  --shadow-card: 0 0.125rem 0.75rem var(--color-pink-shadow);
  --shadow-photo: 0 0.5rem 2rem rgba(0, 0, 0, 0.15);
}

/* Responsive container padding */
@media (max-width: 768px) {
  :root {
    --container-padding: 1.25rem;
  }
}
```

- [ ] **Step 3: Create base styles**

Create `css/base.css`:

```css
@font-face {
  font-family: 'Clash Display';
  src: url('https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap');
  font-display: swap;
}

body {
  font-family: var(--font-body);
  font-size: var(--text-body);
  line-height: var(--leading-normal);
  color: var(--color-slate);
  background-color: var(--color-white);
}

h1, h2, h3 {
  font-family: var(--font-display);
  color: var(--color-ink);
  line-height: var(--leading-snug);
}

h1 {
  font-size: var(--text-hero);
  font-weight: 700;
  letter-spacing: var(--tracking-tight);
}

h2 {
  font-size: var(--text-section);
  font-weight: 700;
}

h3 {
  font-size: var(--text-sub);
  font-weight: 700;
}

.overline {
  font-family: var(--font-body);
  font-size: var(--text-label);
  font-weight: 600;
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-pink);
}

.container {
  max-width: var(--container-max);
  margin: 0 auto;
  padding-left: var(--container-padding);
  padding-right: var(--container-padding);
}

/* Selection color */
::selection {
  background-color: var(--color-pink);
  color: var(--color-white);
}
```

- [ ] **Step 4: Verify in browser**

Create a minimal `index.html` to test the CSS loads:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MsGamer — Paulina Lorné</title>
  <link rel="stylesheet" href="/css/reset.css">
  <link rel="stylesheet" href="/css/tokens.css">
  <link rel="stylesheet" href="/css/base.css">
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&f[]=general-sans@400,500,600&display=swap" rel="stylesheet">
</head>
<body>
  <h1>MsGamer</h1>
  <p class="overline">Design tokens loaded</p>
  <p>Body text in General Sans with slate color.</p>
</body>
</html>
```

Run: `npm run dev`

Expected: Page loads with Clash Display heading, General Sans body text, pink overline, correct colors.

- [ ] **Step 5: Commit**

```bash
git add css/ index.html
git commit -m "feat: add design tokens and CSS foundation"
```

---

### Task 3: Layout Components (Nav + Footer + Sections)

**Files:**
- Create: `css/layout.css`

- [ ] **Step 1: Create layout CSS**

Create `css/layout.css`:

```css
/* ========================================
   NAVIGATION
   ======================================== */

.nav {
  background-color: var(--color-ink);
  padding: 0.875rem var(--container-padding);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav__inner {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: var(--container-max);
  margin: 0 auto;
}

.nav__links-left,
.nav__links-right {
  display: flex;
  gap: 1.75rem;
  font-family: var(--font-body);
  font-size: var(--text-label);
  font-weight: 600;
  letter-spacing: var(--tracking-wide);
  flex: 1;
}

.nav__links-left {
  justify-content: flex-end;
  padding-right: 2.25rem;
}

.nav__links-right {
  justify-content: flex-start;
  padding-left: 2.25rem;
  align-items: center;
}

.nav__link {
  color: rgba(255, 255, 255, 0.55);
  transition: color var(--transition-fast);
}

.nav__link:hover,
.nav__link--active {
  color: var(--color-white);
}

.nav__logo {
  height: 3.5rem;
  width: auto;
  flex-shrink: 0;
}

.nav__social {
  display: flex;
  gap: 0.5rem;
  margin-left: 0.75rem;
}

.nav__hamburger {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  color: var(--color-white);
}

.nav__hamburger-icon {
  display: block;
  width: 1.5rem;
  height: 2px;
  background: currentColor;
  position: relative;
}

.nav__hamburger-icon::before,
.nav__hamburger-icon::after {
  content: '';
  display: block;
  width: 100%;
  height: 2px;
  background: currentColor;
  position: absolute;
  left: 0;
}

.nav__hamburger-icon::before { top: -0.5rem; }
.nav__hamburger-icon::after { top: 0.5rem; }

/* Mobile nav */
.nav__mobile-menu {
  display: none;
  flex-direction: column;
  gap: var(--space-md);
  padding: var(--space-lg) 0;
}

.nav__mobile-menu--open {
  display: flex;
}

@media (max-width: 768px) {
  .nav__inner {
    justify-content: space-between;
  }

  .nav__links-left,
  .nav__links-right {
    display: none;
  }

  .nav__hamburger {
    display: block;
  }

  .nav__logo {
    height: 2.25rem;
  }
}

/* ========================================
   SOCIAL ICON (reusable)
   ======================================== */

.social-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 1.875rem;
  height: 1.875rem;
  border-radius: var(--radius-full);
  font-size: var(--text-label);
  font-weight: 700;
  transition: opacity var(--transition-fast);
}

.social-icon:hover {
  opacity: 0.8;
}

.social-icon--linkedin {
  background-color: var(--color-pink);
  color: var(--color-white);
}

/* Dark background variant */
.social-icon--x-dark {
  background-color: rgba(255, 255, 255, 0.08);
  color: rgba(255, 255, 255, 0.6);
}

/* Light background variant */
.social-icon--x-light {
  background-color: var(--color-blush);
  color: var(--color-pink);
}

/* Larger variant for footer */
.social-icon--lg {
  width: 2.25rem;
  height: 2.25rem;
  font-size: var(--text-small);
}

/* ========================================
   SECTIONS
   ======================================== */

.section {
  padding: var(--space-3xl) var(--container-padding);
}

.section__inner {
  max-width: var(--container-max);
  margin: 0 auto;
}

.section--white { background-color: var(--color-white); }
.section--blush { background-color: var(--color-blush); }
.section--pink {
  background-color: var(--color-pink);
  color: var(--color-white);
}
.section--pink .overline { color: rgba(255, 255, 255, 0.6); }
.section--pink h2, .section--pink h3 { color: var(--color-white); }
.section--pink p { color: rgba(255, 255, 255, 0.8); }

.section--dark {
  background-color: var(--color-ink);
  color: var(--color-white);
}

/* Page hero banners (shorter than homepage hero) */
.hero-banner {
  padding: var(--space-2xl) var(--container-padding);
  background-color: var(--color-blush);
}

.hero-banner__inner {
  max-width: var(--container-max);
  margin: 0 auto;
}

.hero-banner h1 {
  margin-bottom: var(--space-xs);
}

.hero-banner p {
  font-size: var(--text-sub);
  color: var(--color-slate);
}

/* ========================================
   FOOTER
   ======================================== */

.footer {
  background-color: var(--color-ink);
  padding: var(--space-2xl) var(--container-padding);
}

.footer__inner {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-width: var(--container-max);
  margin: 0 auto;
}

.footer__brand {
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 700;
  color: var(--color-pink);
  margin-bottom: var(--space-xs);
}

.footer__links {
  font-size: var(--text-small);
  color: rgba(255, 255, 255, 0.4);
  line-height: 1.8;
}

.footer__links a {
  transition: color var(--transition-fast);
}

.footer__links a:hover {
  color: rgba(255, 255, 255, 0.7);
}

.footer__copyright {
  font-size: var(--text-label);
  color: rgba(255, 255, 255, 0.25);
  margin-top: var(--space-sm);
}

.footer__social {
  display: flex;
  gap: 0.625rem;
}

@media (max-width: 768px) {
  .footer__inner {
    flex-direction: column;
    gap: var(--space-lg);
    align-items: center;
    text-align: center;
  }
}

/* ========================================
   CTA STRIP
   ======================================== */

.cta-strip {
  background-color: var(--color-pink);
  padding: var(--space-2xl) var(--container-padding);
  text-align: center;
}

.cta-strip h2 {
  color: var(--color-white);
  margin-bottom: var(--space-lg);
}
```

- [ ] **Step 2: Build the nav + footer into index.html**

Update `index.html` with the nav and footer markup using the layout classes. Include the real MsGamer logo from `images/logo.png` (download it first — see step 3). Include nav links split around the centered logo and social icons.

- [ ] **Step 3: Download assets**

```bash
mkdir -p images
curl -o images/logo.png "https://msgamer.se/wp-content/uploads/2014/05/logo_400px-300x147.png"
curl -o images/paulina-placeholder.gif "https://www.msgamer.se/wp-content/uploads/2015/10/MsGamerSE.gif"
```

- [ ] **Step 4: Verify nav and footer render correctly**

Run: `npm run dev`

Expected: Dark nav bar with centered logo, flanking links, sticky on scroll. Dark footer with MSGAMER text mark, nav links, social icons. Responsive — collapses to hamburger on mobile (menu toggle comes in Task 8).

- [ ] **Step 5: Commit**

```bash
git add css/layout.css index.html images/
git commit -m "feat: add nav, footer, section layout components"
```

---

### Task 4: Component CSS (Buttons, Cards, Timeline, Portfolio Strip)

**Files:**
- Create: `css/components.css`

- [ ] **Step 1: Create component styles**

Create `css/components.css`:

```css
/* ========================================
   BUTTONS
   ======================================== */

.btn {
  display: inline-block;
  font-family: var(--font-body);
  font-size: var(--text-small);
  font-weight: 700;
  letter-spacing: var(--tracking-wide);
  text-transform: uppercase;
  padding: 0.875rem 2rem;
  border-radius: var(--radius-sm);
  border: none;
  cursor: pointer;
  transition: transform var(--transition-normal), box-shadow var(--transition-normal);
}

.btn:hover {
  transform: scale(1.02);
}

.btn--primary {
  background-color: var(--color-pink);
  color: var(--color-white);
}

.btn--primary:hover {
  box-shadow: 0 0.25rem 1rem rgba(232, 77, 160, 0.3);
}

/* Primary on pink background — inverted */
.btn--primary-inverted {
  background-color: var(--color-white);
  color: var(--color-pink);
}

.btn--primary-inverted:hover {
  box-shadow: 0 0.25rem 1rem rgba(0, 0, 0, 0.15);
}

.btn--secondary {
  background-color: transparent;
  color: var(--color-pink);
  border: 2px solid var(--color-pink);
}

/* Secondary on pink background */
.btn--secondary-inverted {
  background-color: transparent;
  color: var(--color-white);
  border: 2px solid rgba(255, 255, 255, 0.5);
}

.text-link {
  font-family: var(--font-body);
  font-size: var(--text-small);
  font-weight: 600;
  letter-spacing: var(--tracking-wide);
  color: var(--color-pink);
  transition: opacity var(--transition-fast);
}

.text-link::after {
  content: ' →';
}

.text-link:hover {
  opacity: 0.8;
}

/* Text link on pink background */
.text-link--inverted {
  color: var(--color-white);
  border-bottom: 2px solid rgba(255, 255, 255, 0.4);
  padding-bottom: 0.125rem;
}

.text-link--inverted::after {
  content: ' →';
}

/* ========================================
   CAREER CARDS
   ======================================== */

.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

@media (max-width: 1024px) {
  .card-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .card-grid { grid-template-columns: 1fr; }
}

.career-card {
  background-color: var(--color-white);
  border-radius: var(--radius-md);
  padding: var(--space-lg);
  border-top: 4px solid var(--color-pink);
}

.career-card--featured {
  box-shadow: var(--shadow-card);
}

.career-card__date {
  font-family: var(--font-body);
  font-size: var(--text-label);
  font-weight: 600;
  letter-spacing: var(--tracking-wider);
  color: var(--color-pink);
  margin-bottom: var(--space-xs);
}

.career-card__company {
  font-family: var(--font-display);
  font-size: var(--text-sub);
  font-weight: 700;
  color: var(--color-ink);
  margin-bottom: 0.25rem;
}

.career-card__role {
  font-size: var(--text-small);
  color: var(--color-slate);
}

/* ========================================
   PORTFOLIO STRIP
   ======================================== */

.portfolio-strip {
  padding: 1.75rem var(--container-padding);
  background-color: var(--color-white);
  border-bottom: 1px solid #f0f0f0;
  overflow: hidden;
}

.portfolio-strip__inner {
  display: flex;
  align-items: center;
  gap: 2.5rem;
  max-width: var(--container-max);
  margin: 0 auto;
}

.portfolio-strip__label {
  font-family: var(--font-body);
  font-size: var(--text-label);
  font-weight: 600;
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
  color: var(--color-pink);
  white-space: nowrap;
  flex-shrink: 0;
}

.portfolio-strip__track {
  display: flex;
  gap: 1.25rem;
  align-items: center;
  overflow: hidden;
}

.portfolio-strip__brand {
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-ink);
  opacity: 0.5;
  white-space: nowrap;
}

.portfolio-strip__dot {
  color: #e0d0d8;
  flex-shrink: 0;
}

@media (max-width: 768px) {
  .portfolio-strip__inner {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--space-sm);
  }

  .portfolio-strip__track {
    flex-wrap: wrap;
  }
}

/* ========================================
   TIMELINE (Career page)
   ======================================== */

.timeline {
  position: relative;
  padding-left: 2rem;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background-color: var(--color-pink);
  border-radius: 2px;
}

.timeline__entry {
  position: relative;
  padding-bottom: var(--space-2xl);
  padding-left: var(--space-lg);
}

.timeline__entry:last-child {
  padding-bottom: 0;
}

.timeline__dot {
  position: absolute;
  left: calc(-2rem - 5px);
  top: 0.25rem;
  width: 13px;
  height: 13px;
  background-color: var(--color-pink);
  border-radius: var(--radius-full);
  border: 3px solid var(--color-white);
}

.section--blush .timeline__dot {
  border-color: var(--color-blush);
}

.timeline__date {
  font-family: var(--font-body);
  font-size: var(--text-label);
  font-weight: 600;
  letter-spacing: var(--tracking-wider);
  color: var(--color-pink);
  margin-bottom: 0.25rem;
}

.timeline__company {
  font-family: var(--font-display);
  font-size: var(--text-sub);
  font-weight: 700;
  color: var(--color-ink);
  margin-bottom: 0.25rem;
}

.timeline__role {
  font-weight: 600;
  color: var(--color-ink);
  margin-bottom: var(--space-xs);
}

.timeline__description {
  font-size: var(--text-body);
  color: var(--color-slate);
  line-height: var(--leading-normal);
}

/* ========================================
   PRESS CARDS
   ======================================== */

.press-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-md);
}

@media (max-width: 1024px) {
  .press-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 640px) {
  .press-grid { grid-template-columns: 1fr; }
}

.press-card {
  padding: var(--space-lg);
  border: 2px solid var(--color-pink-border);
  border-radius: var(--radius-md);
  text-align: center;
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.press-card:hover {
  border-color: var(--color-pink);
  box-shadow: var(--shadow-card);
}

.press-card__name {
  font-family: var(--font-display);
  font-size: var(--text-body);
  font-weight: 600;
  color: var(--color-ink);
  margin-bottom: 0.25rem;
}

.press-card__type {
  font-size: var(--text-small);
  color: var(--color-slate);
}

/* ========================================
   FEATURED ROLE (Career page)
   ======================================== */

.featured-role {
  background-color: var(--color-white);
  border-radius: var(--radius-lg);
  padding: var(--space-2xl);
  border-top: 4px solid var(--color-pink);
  box-shadow: var(--shadow-card);
}

.featured-role__title {
  font-family: var(--font-display);
  font-size: var(--text-section);
  font-weight: 700;
  color: var(--color-ink);
  margin-bottom: var(--space-xs);
}

.featured-role__company {
  font-size: var(--text-sub);
  font-weight: 600;
  color: var(--color-ink);
  margin-bottom: var(--space-md);
}

.featured-role__description {
  font-size: var(--text-body);
  color: var(--color-slate);
  line-height: var(--leading-normal);
  margin-bottom: var(--space-md);
}

.featured-role__highlights {
  padding-left: var(--space-lg);
}

.featured-role__highlights li {
  list-style: disc;
  color: var(--color-slate);
  margin-bottom: var(--space-xs);
}

.featured-role__highlights li::marker {
  color: var(--color-pink);
}
```

- [ ] **Step 2: Verify components render**

Run: `npm run dev`

Add test markup to `index.html` to verify buttons, cards, and other components render with correct styles. Check at desktop and mobile widths.

- [ ] **Step 3: Commit**

```bash
git add css/components.css
git commit -m "feat: add button, card, timeline, and press card components"
```

---

### Task 5: Animations CSS

**Files:**
- Create: `css/animations.css`

- [ ] **Step 1: Create animation styles**

Create `css/animations.css`:

```css
/* ========================================
   SCROLL REVEAL ANIMATIONS
   ======================================== */

.reveal {
  opacity: 0;
  transform: translateY(1.25rem);
  transition: opacity var(--transition-slow), transform var(--transition-slow);
}

.reveal--visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered children — add to parent, children get delays */
.reveal-stagger > .reveal:nth-child(1) { transition-delay: 0ms; }
.reveal-stagger > .reveal:nth-child(2) { transition-delay: 100ms; }
.reveal-stagger > .reveal:nth-child(3) { transition-delay: 200ms; }
.reveal-stagger > .reveal:nth-child(4) { transition-delay: 300ms; }
.reveal-stagger > .reveal:nth-child(5) { transition-delay: 400ms; }

/* Hero-specific stagger (loads on page load, not scroll) */
.hero__content > * {
  opacity: 0;
  transform: translateY(1rem);
  animation: hero-fade-in 0.6s ease forwards;
}

.hero__content > *:nth-child(1) { animation-delay: 0ms; }
.hero__content > *:nth-child(2) { animation-delay: 100ms; }
.hero__content > *:nth-child(3) { animation-delay: 200ms; }
.hero__content > *:nth-child(4) { animation-delay: 300ms; }

@keyframes hero-fade-in {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ========================================
   PORTFOLIO MARQUEE
   ======================================== */

.marquee {
  display: flex;
  overflow: hidden;
}

.marquee__content {
  display: flex;
  gap: 1.25rem;
  align-items: center;
  animation: marquee-scroll 30s linear infinite;
  white-space: nowrap;
}

.marquee:hover .marquee__content {
  animation-play-state: paused;
}

@keyframes marquee-scroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ========================================
   DECORATIVE CIRCLES (slow drift)
   ======================================== */

.deco-circle {
  position: absolute;
  border-radius: var(--radius-full);
  pointer-events: none;
}

.deco-circle--drift {
  animation: slow-drift 35s ease-in-out infinite alternate;
}

@keyframes slow-drift {
  0% { transform: translate(0, 0); }
  100% { transform: translate(1rem, -0.75rem); }
}

/* ========================================
   TIMELINE DRAW (career page)
   ======================================== */

.timeline--animated::before {
  transform-origin: top;
  transform: scaleY(0);
  transition: transform 1.5s ease;
}

.timeline--animated.timeline--visible::before {
  transform: scaleY(1);
}

/* ========================================
   PHOTO PULSE
   ======================================== */

.hero__photo-frame {
  animation: photo-pulse 2s ease-in-out;
}

@keyframes photo-pulse {
  0% { border-color: rgba(255, 255, 255, 0.2); }
  50% { border-color: rgba(255, 255, 255, 0.5); }
  100% { border-color: rgba(255, 255, 255, 0.2); }
}

/* ========================================
   REDUCED MOTION
   ======================================== */

@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }

  .hero__content > * {
    opacity: 1;
    transform: none;
    animation: none;
  }

  .marquee__content {
    animation: none;
  }

  .deco-circle--drift {
    animation: none;
  }

  .timeline--animated::before {
    transform: scaleY(1);
    transition: none;
  }

  .hero__photo-frame {
    animation: none;
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add css/animations.css
git commit -m "feat: add scroll reveal, marquee, and micro-animation CSS"
```

---

### Task 6: Homepage (index.html)

**Files:**
- Modify: `index.html` (replace test markup with full homepage)

- [ ] **Step 1: Write full homepage HTML**

Replace `index.html` with the complete homepage markup. Include all sections from the design spec:

1. Nav (centered logo, flanked links)
2. Hero (pink background, two-column with photo, decorative circles)
3. Portfolio strip (marquee track with brand names)
4. Career snapshot (blush background, 3 career cards)
5. Gaming Roots teaser (pink background, quote + game controller placeholder)
6. Featured In teaser (white background, 3 press cards)
7. CTA strip (pink background, "Get in touch")
8. Footer (dark, text mark, links, social)

Full SEO meta tags in `<head>`: title, description, Open Graph, Twitter card, canonical URL, JSON-LD Person schema.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MsGamer — Paulina Lorné | Nordic Marketing Manager, Bethesda</title>
  <meta name="description" content="Paulina Lorné (MsGamer) — Nordic Marketing Manager at Bethesda. Driving AAA game launches for Fallout, Starfield, Elder Scrolls, and more across the Nordics.">
  <link rel="canonical" href="https://msgamer.se/">

  <!-- Open Graph -->
  <meta property="og:title" content="MsGamer — Paulina Lorné">
  <meta property="og:description" content="Nordic Marketing Manager at Bethesda. Driving AAA game launches across the Nordics.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://msgamer.se/">
  <meta property="og:image" content="https://msgamer.se/images/og-image.png">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@MsGamerSE">
  <meta name="twitter:title" content="MsGamer — Paulina Lorné">
  <meta name="twitter:description" content="Nordic Marketing Manager at Bethesda. Driving AAA game launches across the Nordics.">

  <!-- Fonts -->
  <link rel="preconnect" href="https://api.fontshare.com" crossorigin>
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&f[]=general-sans@400,500,600&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="/css/reset.css">
  <link rel="stylesheet" href="/css/tokens.css">
  <link rel="stylesheet" href="/css/base.css">
  <link rel="stylesheet" href="/css/layout.css">
  <link rel="stylesheet" href="/css/components.css">
  <link rel="stylesheet" href="/css/animations.css">

  <!-- Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Paulina Lorné",
    "alternateName": "MsGamer",
    "jobTitle": "Nordic Marketing Manager",
    "worksFor": {
      "@type": "Organization",
      "name": "Bethesda Softworks"
    },
    "url": "https://msgamer.se",
    "sameAs": [
      "https://se.linkedin.com/in/paulinalorne",
      "https://twitter.com/MsGamerSE"
    ]
  }
  </script>
</head>
<body>

  <!-- NAVIGATION -->
  <nav class="nav" aria-label="Main navigation">
    <div class="nav__inner">
      <div class="nav__links-left">
        <a href="/" class="nav__link nav__link--active">HOME</a>
        <a href="/about.html" class="nav__link">ABOUT</a>
        <a href="/career.html" class="nav__link">CAREER</a>
      </div>
      <a href="/" aria-label="MsGamer home">
        <img src="/images/logo.png" alt="MsGamer logo" class="nav__logo">
      </a>
      <div class="nav__links-right">
        <a href="/press.html" class="nav__link">PRESS</a>
        <a href="/contact.html" class="nav__link">CONTACT</a>
        <div class="nav__social">
          <a href="https://se.linkedin.com/in/paulinalorne" class="social-icon social-icon--linkedin" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
          <a href="https://twitter.com/MsGamerSE" class="social-icon social-icon--x-dark" aria-label="X (Twitter)" target="_blank" rel="noopener">X</a>
        </div>
      </div>
      <button class="nav__hamburger" aria-label="Open menu" aria-expanded="false">
        <span class="nav__hamburger-icon"></span>
      </button>
    </div>
    <div class="nav__mobile-menu" role="menu">
      <a href="/" class="nav__link nav__link--active" role="menuitem">HOME</a>
      <a href="/about.html" class="nav__link" role="menuitem">ABOUT</a>
      <a href="/career.html" class="nav__link" role="menuitem">CAREER</a>
      <a href="/press.html" class="nav__link" role="menuitem">PRESS</a>
      <a href="/contact.html" class="nav__link" role="menuitem">CONTACT</a>
      <div class="nav__social" style="margin-top: 0.5rem;">
        <a href="https://se.linkedin.com/in/paulinalorne" class="social-icon social-icon--linkedin" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
        <a href="https://twitter.com/MsGamerSE" class="social-icon social-icon--x-dark" aria-label="X (Twitter)" target="_blank" rel="noopener">X</a>
      </div>
    </div>
  </nav>

  <main>
    <!-- HERO -->
    <section class="section section--pink" style="position: relative; overflow: hidden;">
      <!-- Decorative circles -->
      <div class="deco-circle deco-circle--drift" style="top: -3.75rem; right: -2.5rem; width: 17.5rem; height: 17.5rem; border: 2px solid rgba(255,255,255,0.08);"></div>
      <div class="deco-circle deco-circle--drift" style="bottom: -5rem; right: 3.75rem; width: 22.5rem; height: 22.5rem; border: 1px solid rgba(255,255,255,0.05); animation-delay: -10s;"></div>

      <div class="section__inner" style="display: flex; align-items: center; gap: 3rem; position: relative; z-index: 1;">
        <!-- Left: text -->
        <div class="hero__content" style="flex: 1;">
          <p class="overline" style="color: rgba(255,255,255,0.65); margin-bottom: 1.25rem;">Nordic Marketing Manager &bull; Bethesda</p>
          <h1 style="color: var(--color-white);">Marketing leader.<br>Gamer since &rsquo;85.</h1>
          <p style="font-size: var(--text-sub); color: rgba(255,255,255,0.85); line-height: var(--leading-normal); max-width: 32.5rem; margin: 1.5rem 0 2rem;">I drive AAA game launches across the Nordics for Bethesda — Fallout, Starfield, Elder Scrolls, Indiana Jones, and more.</p>
          <div style="display: flex; gap: 0.875rem; flex-wrap: wrap;">
            <a href="/career.html" class="btn btn--primary-inverted">View Career</a>
            <a href="/contact.html" class="btn btn--secondary-inverted">Get in Touch</a>
          </div>
        </div>
        <!-- Right: photo -->
        <div style="flex-shrink: 0; position: relative;">
          <div class="hero__photo-frame" style="width: 16.25rem; height: 16.25rem; border-radius: var(--radius-lg); overflow: hidden; border: 4px solid rgba(255,255,255,0.2); box-shadow: var(--shadow-photo);">
            <img src="/images/paulina-placeholder.gif" alt="Paulina Lorné" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <span style="position: absolute; bottom: -0.75rem; right: -0.75rem; background: var(--color-ink); color: var(--color-white); font-family: var(--font-body); font-size: 0.625rem; font-weight: 600; letter-spacing: 0.125rem; padding: 0.5rem 0.875rem; border-radius: var(--radius-full); box-shadow: 0 0.25rem 0.75rem rgba(0,0,0,0.2);">SINCE '85</span>
        </div>
      </div>
    </section>

    <!-- PORTFOLIO STRIP -->
    <div class="portfolio-strip">
      <div class="portfolio-strip__inner">
        <span class="portfolio-strip__label">Portfolio</span>
        <div class="portfolio-strip__track marquee">
          <div class="marquee__content">
            <span class="portfolio-strip__brand">Fallout</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">Starfield</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">The Elder Scrolls</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">Indiana Jones</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">DOOM</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">Deathloop</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">SteamWorld</span>
            <span class="portfolio-strip__dot">&middot;</span>
            <span class="portfolio-strip__brand">Wolfenstein</span>
          </div>
          <!-- Duplicate for seamless loop — JS will clone this -->
        </div>
      </div>
    </div>

    <!-- CAREER SNAPSHOT -->
    <section class="section section--blush">
      <div class="section__inner reveal-stagger">
        <p class="overline reveal">Career at a Glance</p>
        <h2 class="reveal" style="margin-bottom: 2.25rem;">From community volunteer<br>to AAA launches.</h2>
        <div class="card-grid">
          <div class="career-card career-card--featured reveal">
            <p class="career-card__date">2021 – PRESENT</p>
            <h3 class="career-card__company">Bethesda</h3>
            <p class="career-card__role">Nordic Marketing Manager</p>
          </div>
          <div class="career-card reveal">
            <p class="career-card__date">2019 – 2021</p>
            <h3 class="career-card__company">Thunderful</h3>
            <p class="career-card__role">Marketing Manager</p>
          </div>
          <div class="career-card reveal">
            <p class="career-card__date">2016 – 2019</p>
            <h3 class="career-card__company">Tobii / Image & Form</h3>
            <p class="career-card__role">Marketing Coordinator</p>
          </div>
        </div>
        <a href="/career.html" class="text-link reveal" style="display: inline-block; margin-top: 1.5rem;">View Full Career</a>
      </div>
    </section>

    <!-- GAMING ROOTS TEASER -->
    <section class="section section--pink" style="position: relative; overflow: hidden;">
      <div class="deco-circle" style="bottom: -1.875rem; right: -1.25rem; width: 10rem; height: 10rem; border: 1px solid rgba(255,255,255,0.06);"></div>
      <div class="section__inner" style="display: flex; gap: 3rem; align-items: center; position: relative; z-index: 1;">
        <div style="flex: 1;">
          <p class="overline reveal">Gaming Roots</p>
          <h2 class="reveal" style="margin: 0.75rem 0 1rem;">&ldquo;Some say she should have square eyes. Luckily she didn&rsquo;t listen.&rdquo;</h2>
          <p class="reveal">From AlleyCat on an IBM AT to 400+ hours in Fallout: New Vegas. Not a hobby gamer — a lifer.</p>
          <a href="/about.html" class="text-link text-link--inverted reveal" style="display: inline-block; margin-top: 1.25rem;">Read More</a>
        </div>
        <div class="reveal" style="width: 10rem; height: 10rem; background: rgba(255,255,255,0.1); border-radius: var(--radius-lg); flex-shrink: 0; display: flex; align-items: center; justify-content: center; font-size: 3.25rem;">&#127918;</div>
      </div>
    </section>

    <!-- FEATURED IN TEASER -->
    <section class="section section--white">
      <div class="section__inner">
        <p class="overline reveal">Featured In</p>
        <h2 class="reveal" style="margin-bottom: 1.75rem;">Press & appearances.</h2>
        <div class="press-grid">
          <a href="/press.html" class="press-card reveal">
            <p class="press-card__name">P3 Spel</p>
            <p class="press-card__type">Radio Interview</p>
          </a>
          <a href="/press.html" class="press-card reveal">
            <p class="press-card__name">PAX East</p>
            <p class="press-card__type">Speaker / Organizer</p>
          </a>
          <a href="/press.html" class="press-card reveal">
            <p class="press-card__name">Gamescom</p>
            <p class="press-card__type">Industry Events</p>
          </a>
        </div>
      </div>
    </section>

    <!-- CTA STRIP -->
    <section class="cta-strip">
      <h2>Get in touch.</h2>
      <a href="/contact.html" class="btn btn--primary-inverted">Contact</a>
    </section>
  </main>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer__inner">
      <div>
        <p class="footer__brand">MSGAMER</p>
        <p class="footer__links">
          <a href="/about.html">About</a> &middot;
          <a href="/career.html">Career</a> &middot;
          <a href="/press.html">Press</a> &middot;
          <a href="/contact.html">Contact</a>
        </p>
        <p class="footer__copyright">&copy; 2011–2026 Paulina Lorné. All rights reserved.</p>
      </div>
      <div class="footer__social">
        <a href="https://se.linkedin.com/in/paulinalorne" class="social-icon social-icon--lg social-icon--linkedin" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
        <a href="https://twitter.com/MsGamerSE" class="social-icon social-icon--lg social-icon--x-dark" aria-label="X (Twitter)" target="_blank" rel="noopener">X</a>
      </div>
    </div>
  </footer>

  <!-- Scripts -->
  <script type="module" src="/js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: Verify homepage renders correctly**

Run: `npm run dev`

Expected: Full homepage with all sections. Check: nav logo centered, hero two-column layout, portfolio strip, career cards, gaming roots section, press teaser, CTA strip, footer. Test at 1440px, 768px, and 375px widths.

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: build complete homepage with all sections"
```

---

### Task 7: JavaScript (Scroll Animations, Marquee, Mobile Nav)

**Files:**
- Create: `js/main.js`
- Create: `js/scroll-animations.js`
- Create: `js/marquee.js`
- Create: `js/mobile-nav.js`

- [ ] **Step 1: Create scroll animations module**

Create `js/scroll-animations.js`:

```js
export function initScrollAnimations() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

  if (prefersReducedMotion) {
    document.querySelectorAll('.reveal').forEach(el => {
      el.classList.add('reveal--visible')
    })
    return
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('reveal--visible')
          observer.unobserve(entry.target)
        }
      })
    },
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  )

  document.querySelectorAll('.reveal').forEach(el => {
    observer.observe(el)
  })

  // Timeline draw animation
  const timeline = document.querySelector('.timeline--animated')
  if (timeline) {
    const timelineObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('timeline--visible')
            timelineObserver.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.2 }
    )
    timelineObserver.observe(timeline)
  }
}
```

- [ ] **Step 2: Create marquee module**

Create `js/marquee.js`:

```js
export function initMarquee() {
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  if (prefersReducedMotion) return

  document.querySelectorAll('.marquee').forEach(marquee => {
    const content = marquee.querySelector('.marquee__content')
    if (!content) return

    // Clone content for seamless loop
    const clone = content.cloneNode(true)
    clone.setAttribute('aria-hidden', 'true')
    marquee.appendChild(clone)
  })
}
```

- [ ] **Step 3: Create mobile nav module**

Create `js/mobile-nav.js`:

```js
export function initMobileNav() {
  const hamburger = document.querySelector('.nav__hamburger')
  const menu = document.querySelector('.nav__mobile-menu')

  if (!hamburger || !menu) return

  hamburger.addEventListener('click', () => {
    const isOpen = menu.classList.toggle('nav__mobile-menu--open')
    hamburger.setAttribute('aria-expanded', String(isOpen))
  })

  // Close on link click
  menu.querySelectorAll('.nav__link').forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('nav__mobile-menu--open')
      hamburger.setAttribute('aria-expanded', 'false')
    })
  })

  // Close on escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('nav__mobile-menu--open')) {
      menu.classList.remove('nav__mobile-menu--open')
      hamburger.setAttribute('aria-expanded', 'false')
      hamburger.focus()
    }
  })
}
```

- [ ] **Step 4: Create main entry point**

Create `js/main.js`:

```js
import { initScrollAnimations } from './scroll-animations.js'
import { initMarquee } from './marquee.js'
import { initMobileNav } from './mobile-nav.js'

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations()
  initMarquee()
  initMobileNav()
})
```

- [ ] **Step 5: Verify all interactions work**

Run: `npm run dev`

Test:
1. Scroll down — elements fade in and slide up
2. Portfolio strip scrolls continuously, pauses on hover
3. Resize to mobile — hamburger appears, menu toggles on click, closes on Escape
4. Enable "prefers-reduced-motion" in dev tools — all animations disabled, content visible immediately

- [ ] **Step 6: Commit**

```bash
git add js/
git commit -m "feat: add scroll animations, marquee, and mobile nav JS"
```

---

### Task 8: About Page

**Files:**
- Create: `about.html`

- [ ] **Step 1: Write complete about.html**

Create `about.html` with:

1. Same nav as homepage (with `nav__link--active` on ABOUT)
2. Hero banner — blush background, "Paulina Lorné" heading, subline
3. Bio section — white background, two columns (text left, photo right). Polished first-person rewrite of the original site content. Warm but matching her seniority.
4. Gaming Roots section — blush background. Curated highlights from her gaming history: IBM AT / AlleyCat era, point-and-click adventures, the achievement hunter identity, modern favorites. Visual format — not a wall of text. Consider a tag-cloud or mini-timeline.
5. CTA strip — "Get in touch"
6. Same footer as homepage

Include page-specific SEO meta tags:
- Title: "About — Paulina Lorné (MsGamer) | Nordic Marketing Manager"
- Description: "Meet Paulina Lorné — Nordic Marketing Manager at Bethesda, lifelong gamer, achievement hunter. From AlleyCat on an IBM AT to launching Fallout across the Nordics."

- [ ] **Step 2: Verify about page**

Run: `npm run dev`, navigate to `/about.html`

Expected: Hero banner, bio section with photo, gaming roots section, CTA, footer. Scroll animations trigger. Responsive at all breakpoints.

- [ ] **Step 3: Commit**

```bash
git add about.html
git commit -m "feat: build about page with bio and gaming roots"
```

---

### Task 9: Career Page

**Files:**
- Create: `career.html`

- [ ] **Step 1: Write complete career.html**

Create `career.html` with:

1. Same nav (active on CAREER)
2. Hero banner — "Career" heading, "From community volunteer to AAA launches."
3. Featured Role section — white background. Large card with "CURRENT ROLE" overline, Bethesda / Xbox Game Studios, Nordic Marketing Manager (2021 – Present). Description paragraph + bullet point highlights.
4. Career Timeline — blush background. Vertical pink line with dots. Entries for: Thunderful (2019–2021), Image & Form (2017–2019), Tobii AB (2016–2017), IHM Business School (2014–2016), Community Roots (2011–2015). Each entry has date, company, role, 2-3 line description. Use `timeline--animated` class for the draw effect.
5. CTA strip + footer

Page-specific SEO:
- Title: "Career — Paulina Lorné (MsGamer) | From Community Volunteer to AAA Launches"
- Description: "Paulina Lorné's career journey — from gaming community volunteer to Nordic Marketing Manager at Bethesda, via Thunderful, Tobii, and Image & Form."

- [ ] **Step 2: Verify career page**

Run: `npm run dev`, navigate to `/career.html`

Expected: Featured role card prominent at top. Timeline renders with pink line and dots. Timeline line draws on scroll. Cards fade in. Responsive.

- [ ] **Step 3: Commit**

```bash
git add career.html
git commit -m "feat: build career page with featured role and timeline"
```

---

### Task 10: Press Page

**Files:**
- Create: `press.html`

- [ ] **Step 1: Write complete press.html**

Create `press.html` with:

1. Same nav (active on PRESS)
2. Hero banner — "Press & Appearances" heading, "Events, interviews, and industry moments."
3. Press grid — white background, 3-column responsive grid. Cards for:
   - E3 2019 (Industry Event) — "Attended E3 with Thunderful, met industry leaders"
   - PAX East Boston (Event / Organizer) — "Built and managed booth for Thunderful Publishing"
   - PAX West Seattle (Event) — "Built PAX West booth for Image & Form"
   - Gamescom Cologne (Industry Event) — "Networking and marketing at Europe's largest gaming event"
   - TwitchCon Berlin (Industry Event) — "Represented Thunderful at TwitchCon"
   - P3 Spel (Radio Interview) — "Swedish national radio interview on eye tracking in gaming"
   - Dreamhack Winter (Event) — "Launched HELLFRONT: HONEYMOON, MSI support"
   - EGX Rezzed London (Event) — "Managed booth presence for Zoink!"
   - Dan Bull Collaboration (Collaboration) — "Produced rap video about SteamWorld Quest"
   - ID@Xbox Stockholm (Industry Event) — "Regular attendee at Microsoft's indie showcase"
4. CTA strip + footer

Each card links to an external URL where available (use `#` as placeholder where no URL exists).

Page-specific SEO:
- Title: "Press & Appearances — Paulina Lorné (MsGamer)"
- Description: "Paulina Lorné's industry appearances — E3, PAX, Gamescom, TwitchCon, Dreamhack, and more."

- [ ] **Step 2: Verify press page**

Run: `npm run dev`, navigate to `/press.html`

Expected: Grid of press cards. Hover effect on cards (border color change + shadow). Responsive 3→2→1 columns. Cards fade in on scroll.

- [ ] **Step 3: Commit**

```bash
git add press.html
git commit -m "feat: build press and appearances page"
```

---

### Task 11: Contact Page

**Files:**
- Create: `contact.html`

- [ ] **Step 1: Write complete contact.html**

Create `contact.html` with:

1. Same nav (active on CONTACT)
2. Hero banner — "Get in Touch" heading, "There's no better way to learn new things than to interact with others."
3. Contact section — white background, centered layout:
   - LinkedIn button (primary pink button, opens in new tab)
   - X/Twitter link (text link style, secondary)
   - Email: paulina.lorne@gmail.com (styled as text, mailto: link)
   - Brief friendly text encouraging reaching out
4. Footer (flows directly)

Page-specific SEO:
- Title: "Contact — Paulina Lorné (MsGamer)"
- Description: "Get in touch with Paulina Lorné (MsGamer) — Nordic Marketing Manager at Bethesda. Connect on LinkedIn or reach out via email."

- [ ] **Step 2: Verify contact page**

Run: `npm run dev`, navigate to `/contact.html`

Expected: Centered contact info. LinkedIn button prominent. Links work (LinkedIn, X open in new tabs, email opens mail client). Clean and simple.

- [ ] **Step 3: Commit**

```bash
git add contact.html
git commit -m "feat: build contact page"
```

---

### Task 12: Cross-Page Testing + Polish

**Files:**
- Potentially modify: all HTML and CSS files

- [ ] **Step 1: Test all page navigation**

Run: `npm run dev`

Click through all nav links on every page. Verify:
- Active link highlighting is correct on each page
- All internal links work (no 404s)
- External links (LinkedIn, X) open in new tabs
- Mobile nav works on every page

- [ ] **Step 2: Test responsive breakpoints**

Test every page at:
- 1440px (desktop)
- 1024px (small desktop)
- 768px (tablet)
- 375px (mobile)

Check: hero photo stacks/hides on mobile, career cards reflow, press grid reflows, nav collapses to hamburger, touch targets are 44px+, text remains readable.

- [ ] **Step 3: Test animations**

Verify on every page:
- Scroll reveal triggers once, doesn't re-trigger
- Marquee scrolls smoothly on homepage
- Timeline draws on career page
- Hero fade-in on page load
- All animations disabled with `prefers-reduced-motion: reduce`

- [ ] **Step 4: Test accessibility**

Run Lighthouse accessibility audit on every page.

Check manually:
- Tab through all interactive elements — focus order makes sense, focus indicators visible
- All images have alt text
- Heading hierarchy is correct (h1 → h2 → h3, no skips)
- Color contrast passes (use dev tools)
- Screen reader: nav landmark, main landmark, links are descriptive

Fix any issues found.

- [ ] **Step 5: Run Lighthouse performance audit**

Run: `npm run build && npm run preview`

Open Chrome DevTools → Lighthouse → run Performance, Accessibility, Best Practices, SEO audits on homepage.

Target: 90+ on all four categories. Fix any issues.

- [ ] **Step 6: Validate SEO**

Check on every page:
- Unique `<title>` tag
- Unique `<meta name="description">`
- Open Graph tags present
- Canonical URL correct
- JSON-LD structured data on homepage (validate at search.google.com/structured-data/testing-tool)
- No broken links

- [ ] **Step 7: Commit any fixes**

```bash
git add -A
git commit -m "fix: cross-page polish, accessibility, and performance fixes"
```

---

### Task 13: Production Build + Sitemap

**Files:**
- Create: `public/robots.txt`
- Create: `public/sitemap.xml`

- [ ] **Step 1: Create robots.txt**

Create `public/robots.txt`:

```
User-agent: *
Allow: /

Sitemap: https://msgamer.se/sitemap.xml
```

- [ ] **Step 2: Create sitemap.xml**

Create `public/sitemap.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemapschemas.org/sitemap/0.9">
  <url>
    <loc>https://msgamer.se/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://msgamer.se/about.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://msgamer.se/career.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://msgamer.se/press.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://msgamer.se/contact.html</loc>
    <changefreq>yearly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

- [ ] **Step 3: Run final production build**

```bash
npm run build
```

Expected: Clean build to `dist/` with optimized assets. No errors or warnings.

- [ ] **Step 4: Preview production build**

```bash
npm run preview
```

Navigate through all pages. Everything should work identically to dev mode.

- [ ] **Step 5: Commit**

```bash
git add public/ dist/
git commit -m "feat: add sitemap, robots.txt, and production build"
```

---

## Summary

| Task | Description | Est. Complexity |
|------|-------------|----------------|
| 1 | Project scaffold + Vite | Simple |
| 2 | Design tokens + CSS foundation | Simple |
| 3 | Layout (nav, footer, sections) | Medium |
| 4 | Component CSS (buttons, cards, timeline) | Medium |
| 5 | Animations CSS | Simple |
| 6 | Homepage HTML | Medium |
| 7 | JavaScript modules | Medium |
| 8 | About page | Medium |
| 9 | Career page | Medium |
| 10 | Press page | Simple |
| 11 | Contact page | Simple |
| 12 | Cross-page testing + polish | Medium |
| 13 | Production build + sitemap | Simple |

**Total: 13 tasks.** Phase 2 (WordPress theme conversion) will be a separate plan once Phase 1 is validated.
