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
        user = Profile.objects.get(id=pk)
        topSkills = user.skill_set.exclude(description__exact='')
        otherSkills = user.skill_set.filter(description='')
        content = {
            'user': user,
            'topSkills': topSkills,
            'otherSkills': otherSkills
        }
        return render(request, 'users/user-profile.html', context=content)