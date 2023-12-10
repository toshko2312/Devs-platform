from django.shortcuts import render
from django.http import HttpResponse


class ProjectsCRUD:
    @staticmethod
    def get_single(request, pk: str):
        return render(request, 'projects/single_projects.html', {'pk': pk})

    @staticmethod
    def get_multi(request):
        msg = 'projects'
        number = 11
        projects = [{
            'id': '1',
            'description': 'Description of project 1'},
            {'id': '2',
             'description': 'Description of project 2'
             }]
        content = {'msg': msg,
                   'number': number,
                   'projects': projects}
        return render(request, 'projects/multi_projects.html', context=content)
