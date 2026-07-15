## Logic Review

### Findings

- Severity: High
- File: src/calculator.py
- Description: Calculator division by zero is not handled correctly.
- Evidence: Returning None or passing instead of raising ValueError.
- Recommendation: Ensure that ValueError is raised when dividing by zero.
