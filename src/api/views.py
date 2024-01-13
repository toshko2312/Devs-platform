from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'}
    ]
    return Response(routes)


class ProjectsCRUD:
    @staticmethod
    @api_view(['GET'])
    def get_multi(request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def get_single(request, pk):
        projects = Project.objects.get(id=pk)
        serializer = ProjectSerializer(projects, many=False)
        return Response(serializer.data)
