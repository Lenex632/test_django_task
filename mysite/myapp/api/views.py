from myapp.models import Request, RequestMessage
from myapp.api.serializers import RequestSerializer, MessageSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class RequestListView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetailView(generics.RetrieveAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class MessageListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Request.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        target = self.get_object(pk)
        messages = target.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class CreateRequestView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SendMessageView(generics.CreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        target = Request.objects.get(pk=self.kwargs['pk'])
        serializer.save(request=target)
