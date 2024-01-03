from django.shortcuts import render
from .models import Profile


class UsersCRUD:
    @staticmethod
    def get_multi(request):
        profiles = Profile.objects.all()
        content = {
            'profiles': profiles,
        }
        return render(request, 'users/profiles.html', context=content)

    @staticmethod
    def get_single(request, pk: str):
        return render(request, 'users/user-profile.html')