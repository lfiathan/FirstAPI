#!/bin/sh

set -e # Exit on any command failure

echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
