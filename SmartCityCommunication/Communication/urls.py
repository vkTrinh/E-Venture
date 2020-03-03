from django.urls import path
from . import views
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Project

urlpatterns = [
    path('sender/', views.sender),
    path('addressee/', views.addressee),
    path('projects/', ListView.as_view(queryset=Project.objects.all().order_by("-date")[:25],template_name="Communication/projects.html")),
    path('projects/<int:pk>/', DetailView.as_view(model=Project, template_name="Communication/project.html")),
    path('projects/ranking/', ListView.as_view(queryset=Project.objects.all().order_by("-pro")[:5],template_name="Communication/ranking.html")),
]