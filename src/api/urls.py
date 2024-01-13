from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import get_routes, ProjectsCRUD

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', get_routes),
    path('projects/', ProjectsCRUD.get_multi),
    path('projects/<str:pk>', ProjectsCRUD.get_single),
]