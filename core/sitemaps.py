from django.contrib import sitemaps
from django.urls import reverse

class StaticSitemap(sitemaps.Sitemap):
  def items(self):
    return [
    'index',
    ]
    
  def location(self, item):
    return reverse(item)

sitemaps = {
  'static': StaticSitemap,
}