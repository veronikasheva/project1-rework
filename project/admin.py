from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Contact
from s_content.admin import AdminImageWidget
from django.db import models
from django.utils.html import mark_safe

from django.contrib.auth.models import User, Group


class ItemFeatureAdmin(admin.ModelAdmin):
    pass

class FeatureAdmin(admin.ModelAdmin):
    search_fields = ['title']

class FeatureValueAdmin(admin.ModelAdmin):
    search_fields = ['text']


class ItemAdvantageAdmin(admin.ModelAdmin):
    def show_image(self, obj):
        url = obj.image.url if obj.image else None
        return mark_safe(f'<img src="{url}" style="max-width:150px; height:100px"/>')
    show_image.short_description = "Картинка"
    formfield_overrides = {
        models.ImageField:{'widget': AdminImageWidget},
    }
    fields = ['title', 'image']
    list_display = ['title', 'show_image']

class ItemImageAdmin(admin.ModelAdmin):
    def show_image(self, obj):
        url = obj.image.url if obj.image else None
        return mark_safe(f'<img src="{url}" style="max-width:150px; height:100px"/>')
    show_image.short_description = "Картинка"
    formfield_overrides = {
        models.ImageField:{'widget': AdminImageWidget},
    }
    fields = ['image', 'image_alt']
    list_display = ['show_image', 'image_alt']
    list_editable = ['image_alt']




admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Contact)
