#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'incident_reporting.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))  # Add this line
    print("sys.path:", sys.path)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()