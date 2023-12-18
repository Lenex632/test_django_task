from rest_framework import serializers
from myapp.models import Request, RequestMessage


class RequestSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Request
        fields = ['title', 'description', 'author']


class MessageSerializer(serializers.ModelSerializer):
    request = serializers.ReadOnlyField(source='request.id')

    class Meta:
        model = RequestMessage
        fields = ['text', 'request']
