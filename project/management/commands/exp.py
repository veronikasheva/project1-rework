from django.core.management.base import BaseCommand
from django.apps import apps
from .utils import get_resource, get_file_path, get_folder_path


class Command(BaseCommand):
    help = 'python manage.py exp -path export -format csv'

    def add_arguments(self, parser):
        parser.add_argument('path',  default='project/export', nargs='?', help='path will be created within base_dir')
    
    def handle(self, *args, **kwargs):
        models = apps.get_models()
        for model in models:
            folder_path = get_folder_path(model, kwargs['path'])
            file_path = get_file_path(model, kwargs['path'])
            folder_path.mkdir(parents=True, exist_ok=True)
            resource = get_resource(model)
            data = resource.export().csv
            with open(file_path, 'w', newline='', encoding='utf8') as file:
                file.write(data)
            print(f'{model.__name__:<25} Success!')
