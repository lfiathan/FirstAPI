#!/bin/sh

python manage.py makemigrations myapp && python manage.py migrate

echo "Starting application..."
exec "$@"
