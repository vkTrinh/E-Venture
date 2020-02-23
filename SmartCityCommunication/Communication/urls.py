from django.urls import path
from . import views

urlpatterns = [
    path('sender/', views.sender),
    path('addressee/', views.addressee),
]