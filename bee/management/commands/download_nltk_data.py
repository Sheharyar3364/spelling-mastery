import os
import nltk
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Download necessary NLTK corpora'

    def handle(self, *args, **kwargs):
        # Define a writable directory within your project
        nltk_data_path = os.path.join(settings.BASE_DIR, 'nltk_data')

        # Ensure the directory exists
        os.makedirs(nltk_data_path, exist_ok=True)

        # Append the new path to NLTK's data path
        nltk.data.path.append(nltk_data_path)

        # Add debugging information
        self.stdout.write(f'NLTK data path: {nltk_data_path}')
        self.stdout.write(f'Directory exists: {os.path.exists(nltk_data_path)}')
        self.stdout.write(f'Directory writable: {os.access(nltk_data_path, os.W_OK)}')

        # Attempt to download NLTK data
        try:
            self.stdout.write('Downloading NLTK corpora...')
            nltk.download('brown', download_dir=nltk_data_path)
            nltk.download('gutenberg', download_dir=nltk_data_path)
            nltk.download('reuters', download_dir=nltk_data_path)
            nltk.download('webtext', download_dir=nltk_data_path)
            nltk.download('inaugural', download_dir=nltk_data_path)
            nltk.download('state_union', download_dir=nltk_data_path)
            nltk.download('cmudict', download_dir=nltk_data_path)
            self.stdout.write('Download complete.')
        except Exception as e:
            self.stderr.write(f'Error downloading NLTK corpora: {e}')
