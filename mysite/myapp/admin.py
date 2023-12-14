from django.contrib import admin
from .models import Request, RequestMessage

admin.site.register(Request)
admin.site.register(RequestMessage)
