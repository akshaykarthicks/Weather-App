#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python weathers/manage.py collectstatic --no-input
python weathers/manage.py migrate
