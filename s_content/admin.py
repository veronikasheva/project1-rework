from django.contrib import admin
from .models import Site
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import mark_safe
from django.db import models


class RestrictPermission(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


class AdminImageWidget(AdminFileWidget):
  def render(self, name, value, attrs=None, renderer=None):
    output = []
    if value and getattr(value, "url", None):
      image_url = value.url
      file_name = str(value)
      output.append(
        f' <a href="{image_url}" target="_blank">'
        f'  <img src="{image_url}" alt="{file_name}" width="auto" height="150" '
        f'style="object-fit: cover;"/> </a>')
    output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
    return mark_safe(''.join(output))


@admin.register(Site)
class SiteAdmin(RestrictPermission):
    formfield_overrides = {
        models.ImageField:{'widget': AdminImageWidget},
    }

