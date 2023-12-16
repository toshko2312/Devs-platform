from django.shortcuts import render, redirect

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
    def create(request):
        form = ProjectForm()
        content = {'form': form}

        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('projects')

        return render(request, 'projects/project_form.html', context=content)

    @staticmethod
    def update(request, pk):
        project = Project.objects.get(id=pk)
        form = ProjectForm(instance=project)
        content = {'form': form}

        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                return redirect('projects')

        return render(request, 'projects/project_form.html', context=content)

    @staticmethod
    def delete(request, pk):
        project = Project.objects.get(id=pk)
        content = {'object': project}

        if request.method == 'POST':
            print(request)
            project.delete()
            return redirect('projects')

        return render(request, 'projects/delete_object.html', context=content)
