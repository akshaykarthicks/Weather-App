#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Make sure we're in the directory with manage.py
cd weathers

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate
