from django.urls import path

from .views import get_routes, ProjectsCRUD

urlpatterns = [
    path('', get_routes),
    path('projects/', ProjectsCRUD.get_multi),
    path('projects/<str:pk>', ProjectsCRUD.get_single)

]