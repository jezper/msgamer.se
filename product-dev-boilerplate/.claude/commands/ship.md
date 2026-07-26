# Command: Ship

Full quality pipeline. Execute each step in order. Only proceed to the next step if the previous one passes.

## Steps

1. **Build** — Run `npm run build`. Fix any errors (up to 5 cycles, following build-and-fix skill).
2. **Test** — Run `npm run test`. Fix any failures (up to 3 cycles, following run-tests skill).
3. **Accessibility** — Run the accessibility-check skill on all changed files.
4. **Commit** — Stage and commit with a descriptive message following git-workflow conventions.
5. **Push** — Push to the remote branch.

If any step fails after its retry budget, stop and report. Do not push broken code.
