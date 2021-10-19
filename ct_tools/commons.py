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
