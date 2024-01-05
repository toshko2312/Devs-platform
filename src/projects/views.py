from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm


class ProjectsCRUD:
    @staticmethod
    def get_single(request, pk: str):
        project = Project.objects.get(id=pk)
        content = {
            'project': project
        }
        return render(request, 'projects/single_projects.html', context=content)

    @staticmethod
    def get_multi(request):
        projects = Project.objects.all()
        content = {'projects': projects,
                   'msg': 'Projects'}
        return render(request, 'projects/multi_projects.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def create(request):
        form = ProjectForm()
        content = {'form': form}

        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('projects')

        return render(request, 'projects/project_form.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def update(request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        content = {'form': form}

        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES, instance=project)
            if form.is_valid():
                form.save()
                return redirect('projects')

        return render(request, 'projects/project_form.html', context=content)

    @staticmethod
    @login_required(login_url='login')
    def delete(request, pk):
        project = Project.objects.get(id=pk)
        content = {'object': project}

        if request.method == 'POST':
            project.delete()
            return redirect('projects')

        return render(request, 'projects/delete_object.html', context=content)
