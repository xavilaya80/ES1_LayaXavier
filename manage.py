#!/usr/bin/env python
"""Utilidad de comandos de Django."""

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miproyecto.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        raise ImportError("No se pudo importar Django. Instala requirements.txt.") from error
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
