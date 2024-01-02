from django.contrib import admin
from django.urls import path
from projects.views import ProjectsCRUD

urlpatterns = [
    path('', ProjectsCRUD.get_multi, name='projects'),
    path('create/', ProjectsCRUD.create, name='create-project'),
    path('update/<str:pk>/', ProjectsCRUD.update, name='update-project'),
    path('delete/<str:pk>/', ProjectsCRUD.delete, name='delete-project'),
    path('<str:pk>/', ProjectsCRUD.get_single, name='project')

]