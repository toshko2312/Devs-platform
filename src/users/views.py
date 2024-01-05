from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile, User


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

    @staticmethod
    def login_user(request):
        if request.user.is_authenticated:
            return redirect('users')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exist.')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('users')
            else:
                messages.error(request, 'Incorrect credentials.')

        return render(request, 'users/login_registration.html')

    @staticmethod
    def logout_user(request):
        logout(request)
        messages.success(request, 'Logged out.')
        return redirect('login')
