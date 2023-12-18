from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Request
from .form import RequestForm, MessageForm


@require_POST
def create_request(request):
    author = request.user
    target = None
    form = RequestForm(data=request.POST)
    if form.is_valid():
        target = form.save(commit=False)
        target.author = author
        target.save()

    return render(request, 'myapp/requests/request_create.html', {'target': target, 'form': form})


@require_POST
def send_message(request, request_id):
    target = get_object_or_404(Request, id=request_id)
    message = None
    form = MessageForm(data=request.POST)
    if form.is_valid():
        message = form.save(commit=False)
        message.request = target
        message.save()

    return render(request, 'myapp/requests/message_send.html', {'target': target, 'form': form, 'message': message})


def get_request(request, request_id):
    target = get_object_or_404(Request, id=request_id)
    form = MessageForm

    return render(request, 'myapp/requests/request_detail.html', {'target': target, 'form': form})


def get_request_messages(request, request_id):
    target = get_object_or_404(Request, id=request_id)
    messages = target.messages.all()

    return render(request, 'myapp/requests/messages_list.html', {'target': target, 'messages': messages})


def get_request_list(request):
    requests = Request.objects.all()
    form = RequestForm

    return render(request, 'myapp/requests/requests_list.html', {'requests': requests, 'form': form})
