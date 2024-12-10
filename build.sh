#!/bin/bash
# Build script to handle collectstatic for Django
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear
# 
python manage.py mmigrate