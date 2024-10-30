#!/bin/bash
python manage.py createsuperuser --noinput && python manage.py migrate && python manage.py collectstatic && gunicorn --workers 2 myproject.wsgi 