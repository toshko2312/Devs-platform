from django.contrib import admin
from django.urls import path
from users.views import UsersCRUD

urlpatterns = [
    path('', UsersCRUD.get_multi, name='users'),
    path('profile/<str:pk>/', UsersCRUD.get_single, name='user-profile'),
]
