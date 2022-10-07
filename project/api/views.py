from rest_framework import generics
from rest_framework.response import Response

from django.conf import settings

from .serializers import ContactSerializer
from ..models import Contact
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


class ContactView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        send_mail(
            subject        = 'Отримано контактну форму',
            message= 'Отримано контактну форму',
            html_message   = render_to_string('mail/contact.html', locals()),
            from_email     = settings.DEFAULT_FROM_EMAIL,
            recipient_list = settings.DEFAULT_RECIPIENT_LIST,
            fail_silently  = False,
        )
        return super().post(request, *args, **kwargs)


