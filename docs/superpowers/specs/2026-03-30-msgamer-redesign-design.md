# MsGamer Website Redesign — Design Spec

**Date:** 2026-03-30
**Owner:** Paulina Lorné (msgamer.se)
**Goal:** Redesign msgamer.se from a dated WordPress blog into a modern, professional portfolio site that establishes Paulina as a senior marketing leader in the gaming industry — while keeping the playful personality and pink identity that make her memorable.

---

## 1. Strategic Direction

**Primary purpose:** Professional portfolio — showcasing career, expertise, and credibility to recruiters, employers, and industry peers.

**Secondary purpose:** Personal brand — enough personality and gaming identity that the site feels authentically her, not a generic corporate page.

**Tone of voice:** First-person, warm, polished. Keeps the personality of the original site but tightened up to match her seniority. Not corporate-stiff, not blog-casual.

**Current role:** Nordic Marketing Manager at Bethesda / Xbox Game Studios, overseeing Nordic marketing for Fallout, Starfield, The Elder Scrolls, Indiana Jones, DOOM, Wolfenstein, and more.

---

## 2. Site Structure

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | 30-second pitch — hero statement, career snapshot, gaming roots teaser, press teaser |
| About | `/about` | Polished bio + curated "Gaming Roots" section |
| Career | `/career` | Featured current role (Bethesda) + career timeline |
| Press | `/press` | "Featured In" grid — events, interviews, appearances |
| Contact | `/contact` | LinkedIn (prominent), X (secondary), email |

**Key structural decisions:**
- Old "My Gaming History" page becomes a curated section within About, not its own page
- Old "Highlights" page becomes Career, restructured as featured role + timeline
- Blog replaced with "Featured In" / Press page (lower maintenance, external mentions carry more weight)
- Twitter feed removed entirely
- No contact form — direct to real channels (LinkedIn, email)

---

## 3. Design Direction: Statement Minimal

Clean white canvas with bold pink and dark accents. The pink is confident and deliberate — woven throughout the site, not just spotted on buttons. Professional editorial feel with enough personality to stand out.

### 3.1 Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Hot Pink | `#e84da0` | Primary brand color — nav bar (on dark), hero backgrounds, CTAs, headings, timeline accents, section backgrounds |
| Blush | `#fef7fa` | Alternating section backgrounds, soft accent areas |
| White | `#ffffff` | Primary content backgrounds |
| Ink | `#1a1a2e` | Dark charcoal — nav bar, footer, headlines, body headings |
| Slate | `#6b7280` | Body text |
| Pink Border | `#fce4ef` | Card borders, dividers, subtle pink-tinted lines |

**One pink rule:** Use `#e84da0` consistently everywhere. No gradient mixing, no competing pink shades. Flat, confident, unified.

**Section rhythm:** The page alternates backgrounds: pink → white → blush → pink → white → blush. This weaves pink through the entire experience.

### 3.2 Typography

| Element | Font | Weight | Size | Notes |
|---------|------|--------|------|-------|
| Hero headline | Clash Display | 700 | 50–56px | Letter-spacing: -1.5px. Split-tone: dark for title line, pink for identity line |
| Section heading | Clash Display | 700 | 28–32px | Ink color |
| Subheading | Clash Display | 700 | 18–20px | Used on cards, timeline entries |
| Overline/Label | General Sans | 600 | 11–12px | Uppercase, letter-spacing: 3–4px, pink color |
| Body | General Sans | 400 | 15–17px | Slate color, line-height: 1.7 |
| Nav links | General Sans | 600 | 12px | Uppercase, letter-spacing: 1px |
| CTA buttons | General Sans | 700 | 13px | Uppercase, letter-spacing: 1px |

**Font sources:**
- Clash Display: FontShare (`https://api.fontshare.com/v2/css?f[]=clash-display@600,700`)
- General Sans: FontShare (`https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600`)
- Fallback stack: system-ui, sans-serif

### 3.3 Components

**Buttons:**
- Primary: `#e84da0` background, white text, 4px border-radius, 14px 32px padding
- Secondary: transparent background, `#e84da0` text + 2px border, 4px border-radius
- Text link: `#e84da0` text with arrow (→), no background

**Career cards:**
- White background, 8px border-radius, 4px solid `#e84da0` top border
- Pink overline label (year range), Clash Display company name, General Sans role
- Subtle pink shadow on featured card: `0 2px 12px rgba(232,77,160,0.08)`

**Timeline (Career page):**
- Vertical pink line connecting entries
- Pink dots at each entry
- Alternating white/blush entry backgrounds
- Line draws itself on scroll (animation)

**Social icons:**
- LinkedIn: solid `#e84da0` circle, white icon — prominent
- X: muted circle, subdued icon — secondary
- On dark backgrounds: LinkedIn stays pink, X uses `rgba(255,255,255,0.08)` background
- On light backgrounds: LinkedIn stays pink, X uses `#fef7fa` background with `#e84da0` icon

**Section dividers:**
- No horizontal rules. Background color changes handle visual separation.

### 3.4 Logo

**Primary logo:** Original MsGamer illustrated logo (pink "Ms." script + dark "Gamer" with silhouette figure and gaming button detail). Positioned as a centered centerpiece in the nav bar, with nav links flanking either side.

**Nav layout:** Links split evenly — HOME / ABOUT / CAREER on the left of the logo, PRESS / CONTACT + social icons on the right. Logo at 56px height.

**Footer mark:** Clean "MSGAMER" text in Clash Display, pink color. The typographic version serves as secondary brand mark.

**Mobile nav:** Centered logo with hamburger menu. Logo can scale down to ~36px on small screens.

---

## 4. Page Designs

### 4.1 Homepage

**Sections (top to bottom):**

1. **Navigation bar** — dark charcoal (`#1a1a2e`) background. Original MsGamer logo centered, nav links flanked on either side. Sticky on scroll. A nod to the original site's dark header.

2. **Hero** — flat `#e84da0` background. Two-column layout:
   - Left: Role overline ("NORDIC MARKETING MANAGER • BETHESDA"), Clash Display headline ("Marketing leader. / Gamer since '85."), body paragraph, two CTAs (VIEW CAREER primary, GET IN TOUCH secondary)
   - Right: Photo of Paulina in 260x260px rounded rectangle (16px radius) with subtle white border and shadow. "SINCE '85" dark pill badge at bottom-right corner of photo.
   - Subtle decorative circles (white, low opacity) in background
   - **Note:** Current photo is a placeholder from 2015. Recommend a fresh professional photo before launch — same energy (blazer + gaming tee), just current.

3. **Portfolio strip** — white background. Label "PORTFOLIO" in pink, followed by franchise brand names separated by dots: Fallout · Starfield · The Elder Scrolls · Indiana Jones · DOOM · Deathloop · SteamWorld · Wolfenstein. Names in Clash Display at reduced opacity.

4. **Career snapshot** — blush (`#fef7fa`) background. Section heading "Career at a Glance" / "From community volunteer to AAA launches." Three career cards in a grid: Bethesda (2021–Present), Thunderful (2019–2021), Tobii / Image & Form (2016–2019). Pink top-bordered white cards. "VIEW FULL CAREER →" link below.

5. **Gaming Roots teaser** — flat `#e84da0` background. Quote: "Some say she should have square eyes. Luckily she didn't listen." Short hook text, "READ MORE →" link to About page. Decorative game controller placeholder on right side.

6. **Featured In teaser** — white background. Section heading "Press & appearances." Three cards showing P3 Spel, PAX East, Gamescom with pink-tinted borders.

7. **Footer** — dark charcoal (`#1a1a2e`), matching nav. "MSGAMER" text mark in pink, nav links in muted white, copyright "© 2011–2026 Paulina Lorné", social icons (LinkedIn prominent, X secondary).

### 4.2 About Page

1. **Hero banner** — shorter than homepage, blush background. Clash Display heading: "Paulina Lorné". Subline: "Nordic Marketing Manager at Bethesda. Gamer since the 80s. Glass always half full."

2. **Bio section** — white background. Two columns: polished first-person text on the left, photo on the right. Covers marketing career, gaming passion, what drives her. Warm but professional — rewritten from the original site content to match her current seniority.

3. **Gaming Roots section** — blush background. Curated condensed version of the old Gaming History page. Cherry-picked highlights:
   - Started on an IBM AT with AlleyCat in the 80s
   - The point-and-click adventure era (Monkey Island, King's Quest, Grim Fandango)
   - The achievement hunter identity (400+ hours in Fallout: New Vegas)
   - Modern era favorites (Red Dead 2, God of War, Last of Us)
   - Presented as a visual timeline or scattered "game tag cloud" — not a wall of text

4. **CTA strip** — pink background. "Get in touch" with contact button.

### 4.3 Career Page

1. **Hero banner** — shorter, blush background. Heading: "Career". Subline: "From community volunteer to AAA launches."

2. **Featured Role** — white background, prominent card treatment:
   - Pink overline: "CURRENT ROLE"
   - Company: Bethesda / Xbox Game Studios
   - Title: Nordic Marketing Manager (2021 – Present)
   - Description paragraph covering Nordic marketing for Fallout, Starfield, Elder Scrolls, Indiana Jones, DOOM, etc.
   - Key highlights as bullet points (Deathloop PS5 launch, major DLC campaigns, etc.)
   - Gets significantly more real estate than timeline entries

3. **Career Timeline** — vertical pink line, pink dots, alternating white/blush entries:
   - **Thunderful** (2019–2021) — Marketing Manager / Event & Influencer Manager. 4 title releases, organized first Press Event, PAX, E3, TwitchCon, Gamescom.
   - **Image & Form** (2017–2019) — PR/Marketing. SteamWorld Dig 2 launch, Gamescom.
   - **Tobii AB** (2016–2017) — Marketing Coordinator. Eye-tracking technology.
   - **IHM Business School** (2014–2016) — B2B IT Solutions Sales Representative degree.
   - **Community roots** (2011–2015) — Retrospelsmässan community manager (3000+ visitor convention), EA Sweden volunteer moderator, Zoink Games and Image & Form internships, MSI support at Dreamhack Winter.

4. **CTA strip** — pink background. "Get in touch" with contact button.

### 4.4 Press & Appearances Page

1. **Hero banner** — shorter, blush background. Heading: "Press & Appearances". Subline: "Events, interviews, and industry moments."

2. **Grid of cards** — white background, 2–3 column responsive grid. Each card:
   - White background, `#fce4ef` border, 8px border-radius
   - Event/outlet name in Clash Display
   - Type label (Interview, Event, Talk, Collaboration)
   - Brief 1-line description
   - External link if available
   - Content from existing highlights: PAX East (Boston), Gamescom (Cologne), TwitchCon Berlin, E3 (met Todd Howard, Keanu Reeves), P3 Spel radio interview, Dreamhack Winter, EGX Rezzed (London), Dan Bull rap video collaboration, ID@Xbox Stockholm events

3. **CTA strip** — pink background. "Get in touch" with contact button.

### 4.5 Contact Page

1. **Hero banner** — shorter, blush background. Heading: "Get in Touch". Subline: "There's no better way to learn new things than to interact with others."

2. **Contact section** — white background, centered layout:
   - LinkedIn link — prominent, styled as pink primary button
   - X / Twitter link — secondary, text link style
   - Email: paulina.lorne@gmail.com for professional inquiries
   - No contact form — keeps it simple, directs to real channels

3. **Footer** flows directly since the page is short.

---

## 5. Micro-Animations

All animations respect `prefers-reduced-motion` for accessibility. Subtle, purposeful — enough to make the page feel alive, never distracting.

| Element | Animation | Details |
|---------|-----------|---------|
| Hero text | Staggered fade-in on load | Role label first → headline → body → CTAs. ~100ms delay between each. |
| Portfolio strip | Slow continuous horizontal scroll | Marquee-style, ~30s loop. Pauses on hover. |
| Career cards | Fade up + slide | Triggered on scroll into viewport. Slight upward slide (20px) with opacity fade. |
| Section headings | Gentle fade-in | Triggered on scroll. Simple opacity 0→1 over 400ms. |
| CTA buttons | Scale + shadow lift on hover | Scale to 1.02, shadow deepens. 200ms ease transition. |
| Geometric circle accents | Very slow drift | 30+ second animation loops. Barely perceptible movement. |
| Career timeline line | Draws on scroll | Vertical line extends downward as user scrolls through the timeline. |
| Photo frame | Subtle pulse on load | Single gentle pulse of the white border opacity. |

---

## 6. SEO Strategy

### 6.1 Technical SEO

- **Semantic HTML:** proper `h1` > `h2` > `h3` hierarchy per page, `nav`, `main`, `article`, `section`, `footer` elements
- **Meta tags:** unique `<title>` and `<meta name="description">` per page targeting her name + role + gaming marketing
- **Open Graph + Twitter cards:** proper `og:title`, `og:description`, `og:image`, `twitter:card` tags so shared links display a compelling preview with photo
- **Structured data (JSON-LD):** `Person` schema — name, jobTitle, worksFor (Bethesda), sameAs (LinkedIn, X URLs). Powers Google knowledge panel.
- **Clean URLs:** `/about`, `/career`, `/press`, `/contact`
- **Canonical URLs:** `<link rel="canonical">` on every page
- **Sitemap.xml + robots.txt:** auto-generated, submitted to Google Search Console
- **Mobile-first responsive:** Google indexes mobile version first

### 6.2 Performance

- Critical CSS inlined in `<head>`
- Fonts preloaded via `<link rel="preload">`
- Images in WebP format with fallback, lazy-loaded below the fold
- Descriptive `alt` text on all images
- Minimal JavaScript — animations via CSS where possible, Intersection Observer for scroll triggers

### 6.3 Target Keywords

Primary (natural, not stuffed):
- "Paulina Lorné"
- "MsGamer"
- "Nordic Marketing Manager Bethesda"
- "Gaming marketing Sweden"
- "Game industry marketing"

The site structure and content naturally target these through headings, body text, and meta tags.

---

## 7. Responsive Behavior

| Breakpoint | Behavior |
|------------|----------|
| Desktop (1024px+) | Full layout as described. Centered logo nav with flanked links. |
| Tablet (768–1023px) | Career cards stack to 2-column. Hero photo shrinks. Nav collapses to hamburger. |
| Mobile (< 768px) | Single column throughout. Hero photo stacks above text or hides. Centered logo + hamburger nav. Portfolio strip becomes vertically stacked or hidden. |

- Minimum touch target: 44x44px
- Font sizes in `rem`, not `px`
- Images scale with container

---

## 8. Content Migration Notes

| Source (current site) | Destination | Treatment |
|-----------------------|-------------|-----------|
| Homepage intro text | About page bio | Rewrite: first-person, warm, polished to match seniority |
| "My Gaming History" page | About page "Gaming Roots" section | Condense: cherry-pick strongest beats, visual format |
| "Highlights" timeline (2011–2021) | Career page | Restructure: featured role (Bethesda) + condensed timeline |
| Twitter feed | Removed | Strip entirely. Social links as icons only. |
| Contact info | Contact page | LinkedIn prominent, X secondary, email for inquiries |
| Original MsGamer logo | Nav bar (centered) | Keep as-is. It works with the design. |
| Profile photo (2015) | Hero placeholder | Replace with current professional photo before launch |

---

## 9. Technical Approach

**Phase 1: Static site.** Build as static HTML/CSS/JS with the design system above. Clean, semantic markup. This is the deliverable.

**Phase 2: WordPress theme.** Convert the static site into a WordPress-compatible theme. This allows Paulina to update content (press entries, career updates) through the WordPress admin without touching code.

---

## 10. Pre-Launch Checklist

- [ ] New professional photo taken (recommend: same blazer-over-gaming-tee energy, just current)
- [ ] Bio text reviewed and approved by Paulina
- [ ] Career entries verified for accuracy (dates, titles, company names)
- [ ] Press/appearances list is complete and links work
- [ ] Contact email addresses confirmed as current
- [ ] Portfolio brand list verified with Paulina (any missing or to remove?)
- [ ] WCAG 2.1 AA accessibility audit passed
- [ ] Performance audit (Lighthouse 90+ on all metrics)
- [ ] SEO meta tags and structured data validated
- [ ] Open Graph previews tested on LinkedIn and X
- [ ] Mobile tested on real devices
- [ ] Old WordPress content backed up before theme switch
