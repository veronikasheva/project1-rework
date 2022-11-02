from tabnanny import verbose
from django.db import models

from s_utils.models import AbstractTitleSlug
from s_utils.model_fields import (
    get_image_url,
)



class Contact(models.Model):
    name = models.CharField(verbose_name='Ім\'я', max_length=128, blank=False)
    phone = models.CharField(verbose_name='Телефон', max_length=128, blank=False)
    email = models.TextField(verbose_name='Email', blank=True, null=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"

    def __str__(self):
        return f'{self.name} {self.phone}'


class Year(models.Model):
    name = models.CharField(verbose_name='Рік', max_length=128, blank=False, null=False)
