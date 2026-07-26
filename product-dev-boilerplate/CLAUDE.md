# [PROJECT NAME] — Claude Code Context

## Project overview

<!-- Replace this section with a 2-3 paragraph description of what you're building and why. Focus on the problem being solved, who it's for, and what success looks like. Don't describe the technical implementation — that comes later. -->

**Problem:** [What problem does this solve?]
**For whom:** [Who are the primary users/audiences?]
**Success looks like:** [What outcome means this project succeeded?]

## Stakeholder context

The project owner is a Chief Product Officer with extensive UX design experience. They are not a developer — they build with Claude Code and focus entirely on outcomes and impact. They will never answer questions about how to build things technically.

**Communication rules:**
- When you need stakeholder input, explain in plain everyday language. Frame as product/UX decisions, never engineering decisions.
- When the decision is technical (architecture, patterns, dependencies, file structure), make the call yourself. Full authority. Document reasoning in code comments.
- Only escalate when: the decision changes what a user sees or experiences, there's a scope/timeline trade-off, feature behavior is ambiguous, or something conflicts with the vision.
- The stakeholder may occasionally request specific features — always evaluate whether they align with the stated outcomes. If they don't, say so respectfully and propose alternatives.

## Tech stack

<!-- Fill in your chosen stack. Example below for a typical web app: -->

| Layer | Choice | Why |
|-------|--------|-----|
| Framework | [e.g., Next.js 14+ App Router] | [reason] |
| Language | TypeScript | Type safety |
| Styling | [e.g., Tailwind CSS] | [reason] |
| Database | [e.g., PostgreSQL] | [reason] |
| ORM | [e.g., Prisma] | [reason] |
| Auth | [e.g., NextAuth / Clerk / email-based] | [reason] |
| Deployment | [e.g., Vercel / Railway / AWS] | [reason] |
| Testing | [e.g., Vitest + Playwright] | [reason] |

<!-- If the tech stack hasn't been decided yet, leave this section empty. Claude will propose an appropriate stack based on the project requirements and document reasoning here. -->

## Architecture rules (non-negotiable)

1. **Server components by default.** Use server-side rendering/components for data fetching. Client-side interactivity only when needed (forms, state, event handlers).
2. **API routes for mutations.** All write operations go through API routes with auth checks. Never mutate directly from client components.
3. **Single source of truth.** Every piece of data lives in one place. Views filter and present it differently per audience — they don't duplicate it.
4. **Type safety everywhere.** TypeScript strict mode. No `any` types unless absolutely unavoidable (and documented why).
5. **Environment-driven configuration.** Secrets, feature flags, and environment-specific settings via environment variables. Never hardcoded.

<!-- Add project-specific architecture rules below: -->

## Design principles (non-negotiable)

1. **Outcome over output.** Every feature must serve a clear user outcome. If you can't articulate what behaviour this changes, don't build it.
2. **Calm, purposeful UI.** Generous whitespace. Muted, intentional palette. No animations that delay tasks. No gamification. The tool should feel like a calm workspace.
3. **Progressive disclosure.** Show the minimum needed at each level. Details are available but not imposed.
4. **Accessibility is not optional.** WCAG 2.1 AA minimum. Every release, every component, every time.
5. **Convention over invention.** Follow established web patterns. Only deviate when there's a strong, user-centered reason.

<!-- Add project-specific design principles below: -->

## Accessibility stance (WCAG 2.1 AA — never optional)

These are never optional:
- Every interactive element has a descriptive label for screen readers (visible or aria-label)
- Text scales with system font size preference — never fixed font sizes in px for body text (use rem)
- Color never conveys information alone — always pair with icons, labels, or patterns
- All animations respect `prefers-reduced-motion`
- Touch targets minimum 44x44px
- Focus indicators visible on all interactive elements
- Keyboard navigation works for all interactive flows
- Contrast ratios: 4.5:1 for normal text, 3:1 for large text and UI components

## Color system

<!-- Define your palette here. Use CSS custom properties for theming. Example structure: -->

| Role | Token | Light | Dark | Usage |
|------|-------|-------|------|-------|
| Background primary | `--bg-primary` | `#FFFFFF` | `#111113` | Page background |
| Background secondary | `--bg-secondary` | `#F8F8F7` | `#1A1A1D` | Cards, surfaces |
| Background tertiary | `--bg-tertiary` | `#F0EFED` | `#232326` | Subtle sections |
| Text primary | `--text-primary` | `#1A1A1A` | `#EDEDEC` | Headings, body |
| Text secondary | `--text-secondary` | `#6B6B6B` | `#9B9B9B` | Descriptions, meta |
| Text tertiary | `--text-tertiary` | `#999999` | `#666666` | Hints, timestamps |
| Border default | `--border-default` | `#E5E5E3` | `#2E2E31` | Cards, dividers |
| Border emphasis | `--border-emphasis` | `#D0D0CD` | `#3E3E42` | Hover states |
| Accent primary | `--accent-primary` | `#2563EB` | `#3B82F6` | Links, primary actions |
| Accent success | `--accent-success` | `#16A34A` | `#22C55E` | Success states |
| Accent warning | `--accent-warning` | `#D97706` | `#F59E0B` | Warnings |
| Accent error | `--accent-error` | `#DC2626` | `#EF4444` | Errors, critical |

<!-- Customize colors to match your brand. Always validate contrast ratios in both modes. -->

## Data model summary

<!-- Describe your core entities here. This helps Claude understand the domain when making decisions. Example: -->

<!-- - **User** — Authenticated users with roles and permissions -->
<!-- - **[Entity]** — Description of what it represents and key relationships -->

## Project structure

<!-- Claude will populate this as the project takes shape. Initial structure: -->

```
/
├── CLAUDE.md                    # This file — project context
├── docs/
│   ├── PRD.md                   # Product requirements
│   ├── UX-DESIGN.md             # Interaction and visual design
│   └── ARCHITECTURE.md          # Technical architecture
├── .claude/
│   ├── skills/                  # AI team expertise
│   └── commands/                # Workflow shortcuts
├── src/                         # Source code (structure depends on framework)
├── tests/                       # Test files
├── public/                      # Static assets
└── [config files]               # package.json, tsconfig, etc.
```

## Common patterns

<!-- Document recurring patterns as they emerge. Claude should add to this section as the project evolves. Examples: -->

### How to add a new page
1. Create the route in the appropriate directory
2. Use Server Components for the page, Client Components for interactive sections
3. Add role-based access check if needed
4. Add navigation link
5. Add i18n strings if multi-language
6. Test with keyboard navigation and screen reader before considering complete

### How to add a new feature
Follow the add-feature skill checklist.

## Testing expectations

- Unit tests for all business logic
- Integration tests for all API routes
- E2E tests for critical user flows (Playwright)
- Coverage target: ≥80% on business logic
- Zero failing tests at any time. Fix implementation bugs, don't skip tests.

## What NOT to do

- **Never commit code that doesn't compile.** Build before committing. Always.
- **Never delete or comment out code just to make a build pass.** Fix the root cause.
- **Never delete or skip failing tests to make a test suite green.** Fix the implementation.
- **Never ask the stakeholder about technical decisions.** Make the call, document reasoning.
- **Never use fixed pixel font sizes for body text.** Always `rem` for accessibility.
- **Never add gamification.** No streaks, badges, points, or guilt-inducing language.
- **Never add onboarding wizards.** Use progressive disclosure and contextual hints instead.
- **Never ignore TypeScript errors with `@ts-ignore`.** Fix the types.
- **Never build a feature without understanding what outcome it serves.** Apply the outcome-thinking skill.
- **Never ship without running the accessibility-check skill.** It takes 2 minutes and catches real issues.
