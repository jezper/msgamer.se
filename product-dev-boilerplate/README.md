# Product Development Boilerplate for Claude Code

A comprehensive set of AI team skills, quality gates, and project context files designed for a CPO/product leader who builds with Claude Code. Copy this into any new project directory and you have an instant, high-quality development team.

## What's inside

### CLAUDE.md — The project brain
A template for your project's context file. Fill in the project-specific sections (problem, audience, tech stack) and Claude Code inherits the full set of principles, rules, and patterns. This is the single most important file — it shapes every decision Claude makes.

### .claude/skills/ — Your AI team (20 specialists)

**Product & Strategy (3):**
- `product-designer.md` — JTBD, Kano model, scope management, trade-off decisions
- `outcome-thinking.md` — Applied every time before building. "What behaviour does this change?"
- `product-discovery.md` — Cagan/Torres/Patton discipline. Guards against feature factories.

**Design (4):**
- `ux-designer.md` — Interaction design, information architecture, flow patterns, state design
- `ui-designer.md` — Visual hierarchy, typography, color system, spacing, animation
- `service-designer.md` — End-to-end journey design, touchpoints, multi-role ecosystems
- `ux-researcher.md` — Research methods, heuristic evaluation, synthesis frameworks

**Engineering (6):**
- `frontend-engineer.md` — Component architecture, state management, performance, responsive design
- `backend-engineer.md` — API design, database patterns, auth, security, error handling
- `architect.md` — Tech stack selection, project structure, data model design, dependency management
- `database-designer.md` — Schema design, indexing, migrations, common data patterns
- `infrastructure.md` — Deployment, CI/CD, monitoring, environment management
- `security.md` — OWASP top 10, data handling, file uploads, dependency security

**Quality (5):**
- `accessibility-check.md` — WCAG 2.1 AA checklist (labels, color, sizing, keyboard, motion, semantic HTML)
- `qa-engineer.md` — Testing pyramid, what to test, bug investigation, pre-ship checklist
- `e2e-testing.md` — Playwright best practices, page objects, viewport testing
- `build-and-fix.md` — Build loop with error diagnosis (5 cycle limit)
- `run-tests.md` — Test loop with failure diagnosis (3 cycle limit)

**Operations (4):**
- `git-workflow.md` — Branch conventions, commit standards, conflict resolution
- `add-feature.md` — End-to-end feature implementation checklist
- `new-view.md` — New page/view creation checklist
- `technical-writer.md` — Documentation standards, code comments, ADRs

### .claude/commands/ — Workflow shortcuts (5)
- `/build` — Build and fix errors
- `/test` — Run tests and fix failures
- `/ship` — Full quality pipeline (build → test → accessibility → commit → push)
- `/review` — Pre-commit quality review
- `/e2e` — Run Playwright end-to-end tests

### docs/ — Document templates
- `PRD.md` — Product requirements template
- `ARCHITECTURE.md` — Technical architecture template

## How to use

### Starting a new project

1. **Copy the boilerplate:**
   ```bash
   cp -r product-dev-boilerplate/.claude /path/to/your/new/project/
   cp product-dev-boilerplate/CLAUDE.md /path/to/your/new/project/
   cp -r product-dev-boilerplate/docs /path/to/your/new/project/
   ```

2. **Fill in CLAUDE.md:**
   Open `CLAUDE.md` and fill in the project-specific sections marked with `<!-- comments -->`:
   - Project overview (problem, audience, success criteria)
   - Tech stack (or leave blank for Claude to propose)
   - Architecture rules specific to your project
   - Design principles specific to your project
   - Color system / brand

3. **Fill in the PRD:**
   Open `docs/PRD.md` and describe the problem you're solving. Focus on:
   - What problem exists today
   - Who experiences it
   - What success looks like
   - What's out of scope

4. **Start building:**
   Open Claude Code in your project directory. Claude will read CLAUDE.md and the skills automatically. Just describe what you want in outcome terms:
   - "I want users to be able to submit ideas with zero friction"
   - "The dashboard should answer 'what should we focus on next?' in 10 seconds"
   - "Leadership needs to see progress without learning a new tool"

### Your role as CPO

You focus on:
- **The problem.** What are we solving and for whom?
- **The outcome.** What behaviour should change?
- **The priority.** What matters most right now?
- **The feedback.** Does this feel right? Is it too complex? Too simple?

Claude handles:
- All technical decisions (stack, architecture, patterns)
- All implementation (code, tests, deployment)
- All quality assurance (accessibility, testing, security)
- All documentation (technical docs, code comments)

### When Claude asks you something

Claude will only ask when:
- The decision changes what a user sees or experiences
- There's a scope/timeline trade-off to make
- Feature behavior is ambiguous
- Something conflicts with the stated vision

You'll never be asked about:
- Which library to use
- How to structure the code
- What database pattern to apply
- How to fix a bug

## Customizing

### Adding project-specific skills
Create new `.md` files in `.claude/skills/` for domain-specific knowledge:
- Industry regulations or compliance requirements
- Brand voice and content guidelines
- Specific API integrations your product uses
- Team conventions that differ from the defaults

### Adding project-specific commands
Create new `.md` files in `.claude/commands/` for workflow shortcuts:
- Deploy to staging
- Seed the database with test data
- Generate a changelog
- Run a specific subset of tests

### Evolving the CLAUDE.md
As your project grows, keep CLAUDE.md updated with:
- New common patterns (how to add X, how to modify Y)
- Lessons learned (things that went wrong and how to avoid them)
- Updated data model documentation
- New "what NOT to do" rules based on experience
