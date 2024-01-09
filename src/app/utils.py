from django.core.exceptions import FieldError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_objects(request, model):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    try:
        objects = model.objects.filter(title__icontains=search_query)
    except (AttributeError, FieldError):
        objects = model.objects.filter(name__icontains=search_query)
    return objects, search_query


def pagination(request, objects):
    page = request.GET.get('page')
    p = Paginator(objects, 9)

    try:
        objects = p.page(page)
    except PageNotAnInteger:
        page = 1
        objects = p.page(page)
    except EmptyPage:
        page = p.num_pages
        objects = p.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)
    if right_index > p.num_pages:
        right_index = p.num_pages + 1

    return range(left_index, right_index), objects
