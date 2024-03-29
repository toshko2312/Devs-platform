from django.contrib import admin
from django.urls import path
from users.views import UsersCRUD, SkillsCRUD, MessagesCRUD

urlpatterns = [
    path('login/', UsersCRUD.login_user, name='login'),
    path('logout/', UsersCRUD.logout_user, name='logout'),
    path('register/', UsersCRUD.register_user, name='register'),

    path('', UsersCRUD.get_multi, name='users'),
    path('profile/<str:pk>/', UsersCRUD.get_single, name='user-profile'),
    path('account/', UsersCRUD.account, name='account'),
    path('account/inbox/', MessagesCRUD.get_multi, name='inbox'),
    path('account/inbox/message/<str:pk>/', MessagesCRUD.get_single, name='message'),
    path('account/inbox/message/send/<str:pk>/', MessagesCRUD.create, name='create-message'),
    path('account/edit/', UsersCRUD.edit_account, name='edit-account'),

    path('skill/create/', SkillsCRUD.create, name='create-skill'),
    path('skill/update/<str:pk>/', SkillsCRUD.update, name='update-skill'),
    path('skill/delete/<str:pk>/', SkillsCRUD.delete, name='delete-skill')
]
