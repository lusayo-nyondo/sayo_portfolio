import os
import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Download JavaScript files for HTMX or Alpine.js'

    def add_arguments(self, parser):
        parser.add_argument('package', type=str, choices=['htmx', 'alpine'])
        parser.add_argument('version', type=str)

    def handle(self, *args, **options):
        package = options['package']
        version = options['version']

        if package == 'htmx':
            self.download_package('htmx.org', version)
        elif package == 'alpine':
            self.download_package('alpinejs', version)

    def download_package(self, package_name, version):
        base_url = f'https://unpkg.com/browse/{package_name}@{version}/dist/'
        local_dir = os.path.join(settings.BASE_DIR, 'static', 'js', package_name)

        # Create the directory if it doesn't exist
        os.makedirs(local_dir, exist_ok=True)

        # Get the list of files
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        files = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.js')]

        # Download each file
        for file in files:
            file_url = f'https://unpkg.com/{package_name}@{version}/dist/{file}'
            local_path = os.path.join(local_dir, file)

            response = requests.get(file_url)
            if response.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(response.content)
                self.stdout.write(self.style.SUCCESS(f'Downloaded {file}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download {file}'))

        # Write version to version.txt
        with open(os.path.join(local_dir, 'version.txt'), 'w') as f:
            f.write(version)

        self.stdout.write(self.style.SUCCESS(f'{package_name} version {version} downloaded successfully'))