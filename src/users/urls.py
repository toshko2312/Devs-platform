from django.contrib import admin
from django.urls import path
from users.views import UsersCRUD

urlpatterns = [
    path('login/', UsersCRUD.login_user, name='login'),
    path('logout/', UsersCRUD.logout_user, name='logout'),

    path('', UsersCRUD.get_multi, name='users'),
    path('profile/<str:pk>/', UsersCRUD.get_single, name='user-profile'),
]
