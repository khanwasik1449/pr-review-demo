# Pull Request Review Demo

Welcome to the PR Review Demo application. This project is a simple Python scaffold designed to demonstrate pull request reviews and CI/CD pipelines.

## Project Structure

```text
pr-review-demo/
├── .github/workflows/
│   └── ci.yml
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── authentication.py
│   └── user_management.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_authentication.py
│   └── test_user_management.py
├── pyproject.toml
└── requirements.txt
```

## Setup and Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the test suite:
   ```bash
   pytest
   ```
