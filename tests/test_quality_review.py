import pytest

def test_quality_review_agent_complexity_detection():
    # Arrange: Import QualityReviewAgent from review_bot package
    try:
        from src.review_bot.quality_agent import QualityReviewAgent
    except ImportError:
        pytest.fail("TDD Check: QualityReviewAgent class is not implemented yet in src.review_bot.quality_agent")
        
    agent = QualityReviewAgent()
    
    explore_summary = {
        "pr_title": "Add nested control structures",
        "changed_files": [
            {"file": "src/nested.py", "type": "Source"}
        ]
    }
    # Highly complex and nested logic
    complex_diff = """diff --git a/src/nested.py b/src/nested.py
new file mode 100644
--- /dev/null
+++ b/src/nested.py
@@ -0,0 +1,15 @@
+def do_deep_nesting(x, y, z):
+    if x > 0:
+        if y > 0:
+            for i in range(10):
+                if z > 0:
+                    while True:
+                        if i == 5:
+                            return True
+                        else:
+                            break
+    return False
"""
    # Act: Perform review
    review_output = agent.review(explore_summary=explore_summary, changed_files={"src/nested.py": complex_diff})
    
    # Assert: Output indicates code quality issue (nesting / complexity)
    assert "Code Quality Review" in review_output
    assert "nested.py" in review_output
    assert "nesting" in review_output.lower() or "complexity" in review_output.lower()
    assert "Severity:" in review_output

def test_quality_review_agent_clean():
    # Arrange
    try:
        from src.review_bot.quality_agent import QualityReviewAgent
    except ImportError:
        pytest.fail("TDD Check: QualityReviewAgent class is not implemented yet")
        
    agent = QualityReviewAgent()
    
    # Safe structure using guard clauses
    clean_diff = """diff --git a/src/nested.py b/src/nested.py
new file mode 100644
--- /dev/null
+++ b/src/nested.py
@@ -0,0 +1,5 @@
+def do_simple_logic(x, y, z):
+    # Guard clauses used to prevent nesting
+    if x <= 0 or y <= 0 or z <= 0:
+        return False
+    return True
"""
    # Act
    review_output = agent.review(
        explore_summary={"pr_title": "Guard clause refactor", "changed_files": [{"file": "src/nested.py", "type": "Source"}]},
        changed_files={"src/nested.py": clean_diff}
    )
    
    # Assert
    assert "No code quality issues detected." in review_output
