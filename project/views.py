from django.http import HttpResponse
from django.shortcuts import render

from s_content.models import Site
from .models import Year

def index(request):
    site = Site.objects.first()
    old_years = Year.objects.get(name='Старше')
    years = Year.objects.exclude(name='Старше')
    return render(request, 'index.html', locals())


def robots(request):
    lines = [
        "User-Agent: *",
        "Disallow: /api/",
        "Disallow: /media/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
