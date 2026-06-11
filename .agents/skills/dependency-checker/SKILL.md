---
name: dependency-checker
description: Use when the user asks to check, verify, audit, diagnose, or confirm that required project dependencies are installed, missing, outdated, importable, or available in the current environment.
---

# Dependency Checker

Use this skill to compare a project's declared dependencies with the user's active environment and report exactly what is installed, missing, or suspicious.

## Workflow

1. Identify the project environment.
   - Check the working directory, active virtual environment, runtime version, and package manager.
   - Prefer local manifests such as `requirements.txt`, `pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`, or lockfiles.
   - If multiple ecosystems are present, inspect the files that match the user's request or the app entrypoint.

2. Read declared dependencies.
   - Use the manifest or lockfile instead of guessing from imports when available.
   - For Python, prefer `requirements.txt` first, then `pyproject.toml`, then imports as a fallback.
   - Note optional, development, and runtime dependencies separately when the manifest distinguishes them.

3. Check what is installed.
   - Use package-manager commands that inspect the active environment:
     - Python: `python -m pip list`, `python -m pip show <package>`, or a small import check.
     - Node: `npm ls --depth=0`, `pnpm list --depth=0`, or `yarn list`.
     - Go: `go list -m all`.
     - Rust: `cargo metadata` or `cargo check` when appropriate.
   - Do not install packages unless the user explicitly asks.

4. Verify imports or startup when useful.
   - For Python apps, run targeted import checks for packages whose install names differ from import names.
   - Use the project's lightest safe command, such as a syntax check or dependency-only import command.
   - Avoid commands that start long-running servers unless the user asks.

5. Report results clearly.
   - List installed dependencies that satisfy the manifest.
   - List missing dependencies with the install command needed.
   - List version mismatches or packages that could not be verified.
   - Mention which environment and command were used for the check.

## Python Notes

- Some install names differ from import names, such as `beautifulsoup4` importing as `bs4`.
- `django-environ` imports as `environ`.
- `pypdf`, `docx2txt`, and `unstructured` are often needed by document loaders even when direct imports are not obvious.
- If a project has no test suite, a focused import check is a useful verification step.

## Final Response

Summarize:

- The dependency source checked.
- The environment checked.
- Missing or mismatched packages.
- The exact install command if action is needed.
