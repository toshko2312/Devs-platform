from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Tag
from .forms import ProjectForm, ReviewForm, CreateProjectForm
from app.utils import search_objects, pagination


class ProjectsCRUD:
    @staticmethod
    def get_single(request, pk: str):
        project = Project.objects.get(id=pk)
        form = ReviewForm()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            project.get_vote_count()
            messages.success(request, 'Review submitted')
            return redirect('project', pk=project.id)

        content = {
            'project': project,
            'form': form
        }
        return render(request, 'projects/single_projects.html', context=content)

    @staticmethod
    def get_multi(request):
        projects, search_query = search_objects(request, Project)
        custom_range, projects = pagination(request, projects)

        content = {'objects': projects,
                   'msg': 'Projects',
                   'search_query': search_query,
                   'custom_range': custom_range}
        return render(request, 'projects/multi_projects.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def create(request):
        profile = request.user.profile
        form = CreateProjectForm()
        content = {'form': form}

        if request.method == 'POST':
            new_tags = request.POST.get('newtags').replace(',', ' ').split()
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.owner = profile
                project.save()

                for tag in new_tags:
                    tag, created = Tag.objects.get_or_create(name=tag)
                    project.tags.add(tag)

                return redirect('account')

        return render(request, 'projects/project_form.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def update(request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        form.fields['tags'].queryset = project.tags.all()
        content = {'form': form}

        if request.method == 'POST':
            new_tags = request.POST.get('newtags').replace(',', ' ').split()

            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                project = form.save()
                if not project.image:
                    project.image = 'default.jpg'
                    project.save()
                for tag in new_tags:
                    tag, created = Tag.objects.get_or_create(name=tag)
                    project.tags.add(tag)
                return redirect('account')

        return render(request, 'projects/project_form.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def delete(request, pk):
        profile = request.user.profile
        project = profile.project_set.get(id=pk)
        content = {'object': project}

        if request.method == 'POST':
            project.delete()
            return redirect('account')

        return render(request, 'delete_object.html', context=content)
