from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


class ProjectsCRUD:
    @staticmethod
    def get_single(request, pk: str):
        project = Project.objects.get(id=pk)
        content = {
            'pk': pk,
            'project': project
        }
        return render(request, 'projects/single_projects.html', context=content)

    @staticmethod
    def get_multi(request):
        projects = Project.objects.all()
        content = {'projects': projects,
                   'msg': 'Projects'}
        return render(request, 'projects/multi_projects.html', context=content)
