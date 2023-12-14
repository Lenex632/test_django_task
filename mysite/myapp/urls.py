from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('request_list/', views.get_request_list, name='request_list'),
    path('request_list/<int:request_id>', views.get_request, name='request_detail'),
    path('request_list/<int:request_id>/messages/', views.get_request_messages, name='messages_list'),

    path('request_list/<int:request_id>/send_message/', views.send_message, name='send_message'),
    path('request_list/create_request/', views.create_request, name='create_request'),
]
