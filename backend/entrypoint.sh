#!/bin/sh

python -m manage migrate --no-input
python -m manage collectstatic --no-input

gunicorn backend.wsgi:application --bind 0.0.0.0:8000
