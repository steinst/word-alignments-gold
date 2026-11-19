import subprocess, sys
from pathlib import Path

def test_validate_catalog():
    root=Path(__file__).resolve().parents[1]
    process=subprocess.run([sys.executable,str(root/'scripts/validate.py')],text=True,capture_output=True)
    assert process.returncode == 0, process.stdout + process.stderr
