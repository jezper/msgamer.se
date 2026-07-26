# Command: E2E Tests

Run end-to-end tests with Playwright. Follow the e2e-testing skill for debugging failures.

## Steps

1. **Ensure Playwright is installed:**
   ```bash
   npx playwright install chromium
   ```

2. **Run E2E tests:**
   ```bash
   npx playwright test
   ```

3. If tests fail:
   - Read the error output carefully
   - Check if it's a test issue or an app issue
   - For app issues: fix the application code
   - For test issues: update the test to match intended behavior
   - Re-run. Repeat up to 3 cycles.

4. If tests pass, report success.

5. For visual debugging:
   ```bash
   npx playwright test --headed
   ```
