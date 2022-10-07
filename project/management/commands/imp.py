from .utils import get_resource, get_file_path, order_models
from django.core.management.base import BaseCommand
import tablib
from os import path


class Command(BaseCommand):
    help = 'python manage.py imp -path export -format csv'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str,  default='project/export', help='path will be created within base_dir')
    
    def handle(self, *args, **kwargs):
        models = order_models()
        for model in models:
            file_path = get_file_path(model, kwargs['path'])
            resource = get_resource(model)
            dataset = tablib.Dataset()
            if path.exists(file_path):
                with open(file_path, 'r', newline='', encoding='utf-8') as file:
                    print(f'{model.__name__:>20}')
                    dataset.load(file.read(), format='csv')
                    resource.import_data(dataset, raise_errors=True)
                    print(f'{model.__name__:>20} Success!')
