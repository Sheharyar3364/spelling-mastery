#!/bin/bash

# Install dependencies from requirements.txt
pip install -r requirements.txt && python manage.py download_nltk_data


# Run custom management command to download NLTK data
python manage.py download_nltk_data

# Apply database migrations
python manage.py migrate
