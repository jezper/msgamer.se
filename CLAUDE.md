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
