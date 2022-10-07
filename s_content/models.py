from django.db import models 
from s_utils.models import AbstractMetaTags
from s_utils.model_fields import get_image_url


class AbstractMetaData(models.Model):
	meta_title = models.TextField(verbose_name="Meta-title", blank=True, null=True)
	meta_descr = models.TextField(verbose_name="Meta-description", blank=True, null=True)
	meta_key = models.TextField(verbose_name="Meta-keys", blank=True, null=True)

	class Meta:
		abstract = True


class Site(AbstractMetaData):
  favico = models.ImageField(
      verbose_name="Favico", max_length=512, blank=True, null=True,
      upload_to='site/'
  )
  facebook = models.CharField(
    verbose_name="Facebook", blank=True, null=True, max_length=512
  )
  instagram = models.CharField(
    verbose_name="Instagram", blank=True, null=True, max_length=512
  )
  mail = models.CharField(
    verbose_name="Mail", blank=True, null=True, max_length=512
  )
  phone = models.CharField(
    verbose_name="Phone", blank=True, null=True, max_length=512
  )

  def __str__(self):
    return f'{self.meta_title}'

  class Meta:
      verbose_name = 'Site configuration'
      verbose_name_plural = 'Site configuration'

  def image_url(self):
      return get_image_url(self, 'favico')
