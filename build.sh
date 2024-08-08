#!/bin/bash

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run custom management command to download NLTK data
python3 manage.py download_nltk_data

# Collect static files
python3 manage.py collectstatic --noinput

# Apply database migrations
python3 manage.py migrate
