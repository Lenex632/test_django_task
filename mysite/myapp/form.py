from django import forms
from .models import Request, RequestMessage


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description']


class MessageForm(forms.ModelForm):
    class Meta:
        model = RequestMessage
        fields = ['text']
