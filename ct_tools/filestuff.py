from pathlib import Path
import os
import subprocess
import platform

def open_file(filepath):
    if platform.system() == 'Darwin':       # macOS
        # untested
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        # untested
        os.startfile(filepath)
    else:                                   # linux variants
        filepath = Path(filepath)
        if not filepath.exists():
            os.system(f"touch {filepath}")
        subprocess.call(('xdg-open', filepath))

def fix_suffix(path, default_suffix = ".txt"):
    if default_suffix[0] != ".":
        default_suffix = "." + default_suffix
    path = Path(path)
    if not path.suffix:
        path = Path(str(path) + default_suffix)
    return path
