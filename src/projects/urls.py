from django.contrib import admin
from django.urls import path
from projects.views import ProjectsCRUD

urlpatterns = [
    path('', ProjectsCRUD.get_multi, name='projects'),
    path('project/create/', ProjectsCRUD.create, name='create-project'),
    path('project/<str:pk>/', ProjectsCRUD.get_single, name='project')

]