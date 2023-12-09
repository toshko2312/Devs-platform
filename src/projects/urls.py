from django.contrib import admin
from django.urls import path
from projects.views import ProjectsCRUD

urlpatterns = [
    path('projects/', ProjectsCRUD.get_multi),
    path('project/<str:pk>/', ProjectsCRUD.get_single)
]