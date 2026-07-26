# Command: Review

Review all recent changes for quality. This is a pre-commit review checklist.

## Steps

1. **Check the diff.** Run `git diff` and `git diff --staged`. Read every change.

2. **Code quality:**
   - No `console.log` left in production code
   - No `// @ts-ignore` or `// @ts-expect-error`
   - No commented-out code
   - No hardcoded secrets or credentials
   - No `any` types (search for `: any`)

3. **Outcome check:** For each changed file, apply the outcome-thinking skill. Does this change serve a clear user outcome?

4. **Accessibility check:** Run the accessibility-check skill on all changed UI components.

5. **Type check:** Run `npx tsc --noEmit` and fix any type errors.

6. **Tests:** Run `npm run test` and ensure all pass.

7. **Build:** Run `npm run build` and ensure it succeeds.

8. **Report:** Summarize findings — what looks good, what needs attention.
