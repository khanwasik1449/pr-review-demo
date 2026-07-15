## Security Review

For each issue:

- Severity: Critical
- File: src/database.py
- Issue: Hardcoded credentials
- Evidence: password=secret_pass host=localhost
- Recommendation: Use environment variables or secret vaults instead of hardcoding credentials in source files.
