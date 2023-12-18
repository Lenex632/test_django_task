from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'myapp'

urlpatterns = [
    path('requests/create_request/', views.CreateRequestView.as_view(), name='create_request'),
    path('requests/<pk>/send_message/', views.SendMessageView.as_view(), name='send_message'),

    path('requests/', views.RequestListView.as_view(), name='request_list'),
    path('requests/<pk>/', views.RequestDetailView.as_view(), name='request_detail'),
    path('requests/<pk>/messages/', views.MessageListView.as_view(), name='messages_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
