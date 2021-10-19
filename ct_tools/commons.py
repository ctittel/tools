from datetime import datetime
from pathlib import Path
import os
import subprocess
import platform


def get_isodate():
    return datetime.now().strftime('%Y-%m-%d')


def get_notes_dir():
    notes_dir = os.getenv("NOTES")
    if notes_dir is None:
        raise Exception("$NOTES is not set!")
    return Path(notes_dir)

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
