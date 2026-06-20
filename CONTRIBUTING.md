# Contributing to DocSage

Thank you for your interest in contributing to DocSage.

## Development setup

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
python create_relational_db.py
```

## Running tests

```bash
pytest
```

Tests use a temporary SQLite file via `DOC_SAGE_DB_PATH` — no `.env`, API keys, or GGUF model required.

## Code quality

Install and run pre-commit hooks before committing:

```bash
pre-commit install
pre-commit run --all-files
```

Pre-commit runs ruff (lint + format), mypy, pytest, gitleaks, pip-audit, and pyrefly.

## Pull request workflow

1. Fork the repository on GitLab.
2. Create a feature branch from `main`.
3. Make your changes with tests where applicable.
4. Ensure `pytest` and `pre-commit run --all-files` pass.
5. Open a merge request with a clear description of the change.

## What not to commit

- `.env` or real API keys
- `doc_sage.sqlite`, `persist/`, `sections/`, `temp_files/`
- `__pycache__/` and other build artifacts

## License

By contributing, you agree that your contributions will be licensed under the GNU Affero General Public License v3.0.
