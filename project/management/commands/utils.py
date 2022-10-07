from os import PathLike

from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from import_export.resources import ModelResource
from django.conf import settings
from django.apps import apps
from django.db.models import Model
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from import_export.results import RowResult

from typing import List, Optional, Union

BASE_DIR = settings.BASE_DIR
EXCLUDE_MODELS = [Session, ContentType, Permission]



def get_file_path(model: Model, path: Union[str, PathLike]) -> PathLike:
    label = model._meta.label
    folder_label = label[:label.rfind('.')]
    file_name = label[label.rfind('.') + 1:] + '.csv'
    file_path = BASE_DIR / path / folder_label / file_name
    return file_path


def get_folder_path(model: Model, path: Union[str, PathLike]) -> PathLike:
    label = model._meta.label
    folder_label = label[:label.rfind('.')]
    folder_path = BASE_DIR / path / folder_label
    return folder_path


def get_resource(model: Model) -> ModelResource:
    resource = resources.modelresource_factory(model=model)
    resource.Meta.model = model
    resource.Meta.fields = []
    concrete_fields = model._meta.concrete_fields
    for field in model._meta.get_fields():
        if field in concrete_fields:
            if field.many_to_many:
                resource.Meta.fields.append(field.name)
                related_model = field.related_model
                setattr(resource, field.name, fields.Field(
                    widget=ManyToManyWidget(related_model)))
            else:
                resource.Meta.fields.append(field.name)
    return resource()


def get_model_properties(models): 
  objects = []
  for model in models:
     obj = {
       'model': model,
       'one_to_many': False, 
       'one_to_one': False, 
       'many_to_many': False, 
       'many_to_one': False, 
       'relation': False, 
       'position': 1
       }
     fields = model._meta.get_fields()
     for field in fields:
       if field.one_to_many: 
         obj['one_to_many'] = True
       if field.one_to_one: 
         obj['one_to_one'] = True
       if field.many_to_many: 
         obj['many_to_many'] = True
       if field.many_to_one: 
         obj['many_to_one'] = True

       if field.is_relation:
         obj['relation'] = True
     if obj.get('many_to_many') or obj.get('one_to_one') and not obj.get('one_to_many') and not obj.get('many_to_one'): 
       obj['relation'] = False
     objects.append(obj)
  return objects


def get_next_models(models_prop, next_models, counter, chains):
    models = [model.get('model') for model in next_models]
    next_models = []
    for model in models:
        for field in model._meta.get_fields():
            if field.one_to_many:
                next_models.append(
                    next(
                        (x for x in models_prop if x.get(
                            'model') == field.related_model)
                    )
                )
    [model_prop.update({'positions': counter}) for model_prop in next_models]
    if next_models not in chains:
        return next_models
    else:
        return []


def recursion(models_prop, next_models=[], chains=[], counter=1):
    counter += 1
    next_models = get_next_models(models_prop, next_models, counter, chains)
    if not next_models:
        return chains
    else:
        chains.append(next_models)
        return recursion(models_prop, next_models=next_models, chains=chains, counter=counter)


def order_models():
    ordered_models = []
    models = apps.get_models()
    models_properties = get_model_properties(models)
    without_relation = [obj for obj in models_properties if obj.get('relation') is False]
    zero_models = [obj for obj in models_properties if obj.get('one_to_many') is True and obj.get('many_to_one') is False]
    model_prop_chains = [chain_list for chain_list in [recursion(models_properties, next_models=[zero_model]) for zero_model in zero_models]]
    all_model_props_with_positions = [model_prop for lst in model_prop_chains for model_prop in lst]
    _sorted = sorted([model_prop for lst in all_model_props_with_positions for model_prop in lst], key=lambda x: x['position'], reverse=True)
    print([i['model'] for i in without_relation])
    [_sorted.insert(0, x) for x in zero_models if x not in _sorted]
    [_sorted.insert(0, x) for x in without_relation if x not in _sorted]
    excluded = []
    [excluded.append(x.get('model')) for x in _sorted if x.get('model') not in excluded]
    ordered_models.extend(excluded)
    return [model for model in ordered_models if model not in EXCLUDE_MODELS]

