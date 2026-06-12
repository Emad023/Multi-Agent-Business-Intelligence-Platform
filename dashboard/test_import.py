# dashboard/test_import.py

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from workflow.langgraph_orchestrator import app

print("Import Successful")