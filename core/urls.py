from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
from project.views import robots


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('project.api.urls')),
    path('', include('project.urls'), name='project'),
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots, name='robots'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
