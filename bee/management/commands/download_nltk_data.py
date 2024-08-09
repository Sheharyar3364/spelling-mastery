import os
import nltk
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Download necessary NLTK corpora'

    def handle(self, *args, **kwargs):
        nltk_data_path = os.path.join(settings.BASE_DIR, 'nltk_data')
        os.makedirs(nltk_data_path, exist_ok=True)
        nltk.data.path.append(nltk_data_path)
        
        self.stdout.write('Downloading NLTK corpora...')
        nltk.download('brown', download_dir=nltk_data_path)
        nltk.download('gutenberg', download_dir=nltk_data_path)
        nltk.download('reuters', download_dir=nltk_data_path)
        nltk.download('webtext', download_dir=nltk_data_path)
        nltk.download('inaugural', download_dir=nltk_data_path)
        nltk.download('state_union', download_dir=nltk_data_path)
        nltk.download('cmudict', download_dir=nltk_data_path)
        self.stdout.write('Download complete.')
