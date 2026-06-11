---
name: bug-fixer
description: Use when the user asks to fix, debug, investigate, reproduce, diagnose, or resolve a bug, failing test, crash, exception, regression, broken behavior, or incorrect output in a codebase.
---

# Bug Fixer

Use this skill to move from a vague symptom to a verified fix without widening the change more than necessary.

## Workflow

1. Establish the symptom.
   - Read the user report, logs, stack traces, screenshots, failing tests, and recent diffs.
   - If the report is ambiguous, inspect the code first and ask only for missing information that blocks reproduction.

2. Reproduce or localize.
   - Prefer an existing failing test, command, page, or workflow that demonstrates the bug.
   - If reproduction is expensive, narrow the likely failure path with targeted searches and file reads.
   - Identify the smallest component responsible before editing.

3. Find the root cause.
   - Trace data flow, state changes, boundary conditions, and external inputs.
   - Check recent changes when the issue looks like a regression.
   - Distinguish the actual cause from nearby symptoms.

4. Patch narrowly.
   - Keep the edit scoped to the failing behavior.
   - Follow existing project patterns and helper APIs.
   - Avoid unrelated cleanup, formatting churn, or broad rewrites.

5. Add or update coverage when useful.
   - Add a focused regression test when the project has a relevant test setup.
   - If no test framework exists, use the smallest practical verification command or manual check.

6. Verify.
   - Run the failing test or reproduction again.
   - Run nearby tests or a syntax/build check when the change touches shared code.
   - Report what passed and any verification that could not be run.

## Debugging Heuristics

- Start with the exact error message or incorrect output, then work backward.
- Search for the affected function, route, component, query, or config key.
- Inspect call sites before changing a shared helper.
- Validate assumptions with small commands instead of guessing.
- Treat generated files, databases, caches, and local artifacts as suspect unless the bug is explicitly about them.

## Final Response

Summarize:

- The root cause.
- The fix made.
- The verification performed.
- Any remaining risk or follow-up that matters.
