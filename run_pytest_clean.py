import pytest
import sys

with open("pytest_clean_output.txt", "w") as f:
    sys.stdout = f
    sys.stderr = f
    pytest.main(["tests/test_langgraph_orchestrator.py", "-v", "--color=no"])
