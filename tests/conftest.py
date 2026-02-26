import sys
from pathlib import Path

# Add src directory to sys.path to import the oee package
sys.path.append(str((Path(__file__).resolve().parents[1] / "src")))
