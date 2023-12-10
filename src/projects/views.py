from django.shortcuts import render
from django.http import HttpResponse


class ProjectsCRUD:
    @staticmethod
    def get_single(request, pk: str):
        return render(request, 'projects/single_projects.html')

    @staticmethod
    def get_multi(request):
        return render(request, 'projects/multi_projects.html')
