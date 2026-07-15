class FinalReviewAgent:
    """Aggregates findings from all review subagents, deduplicates, and compiles the final report."""

    def aggregate(self, logic: str, security: str, test: str, quality: str, dependency: str, cicd: str, docs: str) -> str:
        # Determine overall risk
        all_inputs = f"{logic}\n{security}\n{test}\n{quality}\n{dependency}\n{cicd}\n{docs}"
        
        has_critical = "severity: critical" in all_inputs.lower() or "critical" in all_inputs.lower()
        has_high = "severity: high" in all_inputs.lower() or "high" in all_inputs.lower()
        
        if has_critical:
            overall_risk = "High"
            recommendation = "Request Changes"
        elif has_high:
            overall_risk = "High"
            recommendation = "Request Changes"
        elif "needs improvement" in all_inputs.lower() or "warning" in all_inputs.lower():
            overall_risk = "Medium"
            recommendation = "Approve with Comments"
        else:
            overall_risk = "Low"
            recommendation = "Approve"
            
        def clean_section(content, prefix_to_remove):
            cleaned = content
            for prefix in prefix_to_remove:
                cleaned = cleaned.replace(prefix, "")
            return cleaned.strip()

        logic_part = clean_section(logic, ["## Logic Review\n\n### Findings\n\n", "## Logic Review\n\n"])
        security_part = clean_section(security, ["## Security Review\n\n", "## Security Review\n"])
        test_part = clean_section(test, ["## Test Review\n\n", "## Test Review\n"])
        quality_part = clean_section(quality, ["## Code Quality Review\n\n### Findings\n\n", "## Code Quality Review\n\n"])
        dependency_part = clean_section(dependency, ["## Dependency Review\n\n### Findings\n\n", "## Dependency Review\n\n"])
        cicd_part = clean_section(cicd, ["## CI/CD Review\n\n### Findings\n\n", "## CI/CD Review\n\n"])
        docs_part = clean_section(docs, ["## Documentation Review\n\n", "## Documentation Review\n"])
        
        report = []
        report.append("# Pull Request Review\n")
        report.append("## Summary\n")
        report.append(f"Overall Risk: {overall_risk}\n")
        report.append("## Findings\n")
        
        report.append("### Logic")
        report.append(logic_part)
        
        report.append("\n### Security")
        report.append(security_part)
        
        report.append("\n### Tests")
        report.append(test_part)
        
        report.append("\n### Code Quality")
        report.append(quality_part)
        
        report.append("\n### Dependencies")
        report.append(dependency_part)
        
        report.append("\n### CI/CD")
        report.append(cicd_part)
        
        report.append("\n### Documentation")
        report.append(docs_part)
        
        report.append("\n## Recommendation\n")
        report.append(f"- {recommendation}")
        
        return "\n".join(report)
