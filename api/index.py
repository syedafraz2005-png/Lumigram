import os
import sys
from pathlib import Path

# Add the Django project root (where manage.py and Lumigram/ reside) to sys.path
PROJECT_DIR = Path(__file__).resolve().parent.parent / 'Lumigram'
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

# Handle SQLite database copying to writable /tmp directory on Vercel serverless environment
if os.environ.get('VERCEL'):
    import shutil
    tmp_db = Path('/tmp/db.sqlite3')
    orig_db = PROJECT_DIR / 'db.sqlite3'
    if not tmp_db.exists() and orig_db.exists():
        try:
            shutil.copyfile(orig_db, tmp_db)
        except Exception as e:
            print("Error copying db.sqlite3 to /tmp:", e)

from Lumigram.wsgi import app
