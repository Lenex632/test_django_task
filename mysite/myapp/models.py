from django.db import models
from django.contrib.auth.models import User


class Request(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')

    objects = models.Manager()


class RequestMessage(models.Model):
    text = models.TextField()
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='messages')

    objects = models.Manager()
