from django.core.exceptions import FieldError


def search_objects(request, model):
    search_query = ''

    if request.GET:
        search_query = request.GET.get('search_query')
        print(search_query)

    try:
        objects = model.objects.filter(name__icontains=search_query)
    except (AttributeError, FieldError):
        objects = model.objects.filter(title__icontains=search_query)
    return objects, search_query
