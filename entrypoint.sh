#!/bin/sh

set -e

echo "Applying database migrations..."
python manage.py migrate

echo "Starting Django server..."
exec python -u manage.py runserver 0.0.0.0:8000 --noreload
