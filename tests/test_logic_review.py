import pytest
import json
import os

def test_logic_review_agent_bug_detection():
    # Arrange: Import LogicReviewAgent from review_bot package
    try:
        from src.review_bot.logic_agent import LogicReviewAgent
    except ImportError:
        pytest.fail("TDD Check: LogicReviewAgent class is not implemented yet in src.review_bot.logic_agent")
    
    agent = LogicReviewAgent()
    
    # Resolve fixture paths
    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
    metadata_path = os.path.join(fixtures_dir, "sample_bug_pr", "metadata.json")
    diff_path = os.path.join(fixtures_dir, "sample_bug_pr", "diff.patch")
    
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
        
    with open(diff_path, "r") as f:
        diff_content = f.read()
        
    # Act: Perform review on the bug PR diff
    review_output = agent.review(explore_summary=metadata, changed_files={"src/calculator.py": diff_content})
    
    # Assert: Verify structure and findings match expectations
    assert "Logic Review" in review_output
    assert "calculator.py" in review_output
    assert "ValueError" in review_output or "division by zero" in review_output.lower()
    assert "Severity:" in review_output

def test_logic_review_agent_no_bugs():
    # Arrange
    try:
        from src.review_bot.logic_agent import LogicReviewAgent
    except ImportError:
        pytest.fail("TDD Check: LogicReviewAgent class is not implemented yet")
        
    agent = LogicReviewAgent()
    
    # A safe diff without logic bugs
    clean_diff = """diff --git a/src/calculator.py b/src/calculator.py
--- a/src/calculator.py
+++ b/src/calculator.py
@@ -4,3 +4,3 @@ class Calculator:
     def add(self, a: float, b: float) -> float:
-        return a + b
+        return a + b
"""
    # Act
    review_output = agent.review(
        explore_summary={"pr_title": "Clean Refactor", "changed_files": [{"file": "src/calculator.py", "type": "Source"}]},
        changed_files={"src/calculator.py": clean_diff}
    )
    
    # Assert
    assert "No logic issues detected." in review_output
