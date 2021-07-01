#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# - Models (see below):
#     - Invoices-Model
#     - Contracts-Model
# - Task:
#     - DRF-End point "Rechnung"
#         - List: All Invoices
#         - View: Invoice detail
#         - Update: Invoice.draft (HTTP Patch)
#         - List-Filters:
#             Billed: yes/no,
#             Invoice for a contract or invoice for several contracts,
#             All invoices for a given creation date
#     - Use DRF-Serializer
    
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
