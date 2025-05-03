#!/usr/bin/env python
import os
import sys

def main():
    """نقطه ورود به اسکریپت مدیریت Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_root.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "ماژول Django یافت نشد. مطمئن شوید که پکیج‌ها نصب شده‌اند."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()