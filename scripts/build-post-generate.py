import platform
import shutil
from pathlib import Path

# Paths
dist_dir = Path("dist")
output_dir = Path("dist_out")
output_dir.mkdir(exist_ok=True)

# Detect OS
is_windows = platform.system() == "Windows"

# Source binary
src = dist_dir / ("run.exe" if is_windows else "run")
dst = output_dir / ("task-todos.exe" if is_windows else "task-todos")

# Move/rename binary
if src.exists():
    shutil.move(str(src), str(dst))
    print(f"Moved {src} to {dst}")
else:
    print(f"Error: Expected binary not found at {src}")
    exit(1)
