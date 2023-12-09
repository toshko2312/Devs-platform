from django.shortcuts import render
from django.http import HttpResponse


class ProjectsCRUD:
    @staticmethod
    def get_single(request, pk: str):
        return HttpResponse(f'Single project #{pk}')

    @staticmethod
    def get_multi(request):
        return HttpResponse('All products')
