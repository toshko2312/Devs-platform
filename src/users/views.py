from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import Profile, User, Message
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from app.utils import search_objects, pagination


class UsersCRUD:
    @staticmethod
    def get_multi(request):
        profiles, search_query = search_objects(request, Profile)
        custom_range, profiles = pagination(request, profiles)
        content = {
            'objects': profiles,
            'search_query': search_query,
            'custom_range': custom_range
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
        page = 'login'
        content = {'page': page}

        if request.user.is_authenticated:
            return redirect('users')

        if request.method == 'POST':
            username = request.POST['username'].lower()
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exist.')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect(request.GET['next'] if 'next' in request.GET else 'account')
            else:
                messages.error(request, 'Incorrect credentials.')

        return render(request, 'users/login_registration.html', context=content)

    @staticmethod
    def logout_user(request):
        logout(request)
        messages.info(request, 'Logged out.')
        return redirect('login')

    @staticmethod
    def register_user(request):
        page = 'register'
        form = CustomUserCreationForm()
        content = {'page': page,
                   'form': form}

        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()

                messages.success(request, 'User account was created!')
                login(request, user)
                return redirect('edit-account')
            else:
                messages.error(request, 'An error has occurred during registration.')

        return render(request, 'users/login_registration.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def account(request):
        profile = request.user.profile

        content = {'profile': profile}
        return render(request, 'users/account.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def edit_account(request):
        form = ProfileForm(instance=request.user.profile)

        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                profile = form.save()
                if not profile.image:
                    profile.image = 'profiles/user-default.png'
                    profile.save()
                return redirect('account')

        content = {'form': form}
        return render(request, 'users/profile_form.html', context=content)


class MessagesCRUD:
    @staticmethod
    @login_required(login_url='login')
    def get_multi(request):
        profile = request.user.profile
        user_messages = profile.messages.all()
        unread_count = user_messages.filter(is_read=False).count()
        content = {'user_messages': user_messages,
                   'unread_count': unread_count}
        return render(request, 'users/inbox.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def get_single(request, pk):
        user_message = request.user.profile.messages.get(id=pk)
        if not user_message.is_read:
            user_message.is_read = True
            user_message.save()
        content = {'user_message': user_message}
        return render(request, 'users/message.html', context=content)

    @staticmethod
    def create(request, pk):
        recipient = Profile.objects.get(id=pk)
        form = MessageForm()

        try:
            sender = request.user.profile
        except:
            sender = None

        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                user_message = form.save(commit=False)
                user_message.sender = sender
                user_message.recipient = recipient

                if sender:
                    user_message.name = sender.name
                    user_message.email = sender.email
                user_message.save()
                messages.success(request, 'Message sent')
                return redirect('user-profile', pk=pk)

        content = {'pk': pk,
                   'form': form}
        return render(request, 'users/message_form.html', context=content)


class SkillsCRUD:
    @staticmethod
    @login_required(login_url='login')
    def create(request):
        profile = request.user.profile
        form = SkillForm()
        content = {'form': form}

        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                skill = form.save(commit=False)
                skill.owner = profile
                skill.save()
                messages.success(request, 'Skill was successfully added!')
                return redirect('account')

        return render(request, 'users/skill_form.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def update(request, pk):
        profile = request.user.profile
        skill = profile.skill_set.get(id=pk)
        form = SkillForm(instance=skill)
        content = {'form': form}

        if request.method == 'POST':
            form = SkillForm(request.POST, instance=skill)
            if form.is_valid():
                form.save()
                messages.success(request, 'Skill was successfully updated!')
                return redirect('account')

        return render(request, 'users/skill_form.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def delete(request, pk):
        profile = request.user.profile
        skill = profile.skill_set.get(id=pk)
        content = {'object': skill}
        if request.method == 'POST':
            skill.delete()
            messages.success(request, 'Skill was successfully deleted!')
            return redirect('account')
        return render(request, 'delete_object.html', context=content)
