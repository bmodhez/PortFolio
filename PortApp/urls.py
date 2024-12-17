from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('contactme/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
]