from django.core.management.base import BaseCommand
import nltk
import os

class Command(BaseCommand):
    help = 'Download necessary NLTK corpora'

    def handle(self, *args, **kwargs):
        nltk_data_path = '/mnt/persistent/nltk_data'
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
