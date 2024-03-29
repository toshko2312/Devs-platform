from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProjectSerializer, ProfileSerializer
from projects.models import Project, Review
from users.models import Profile


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

    @staticmethod
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def vote(request, pk):
        project = Project.objects.get(id=pk)
        user = request.user.profile
        data = request.data
        review, created = Review.objects.get_or_create(
            owner=user,
            project=project
        )

        review.value = data['value']
        review.save()
        project.get_vote_count()

        serializer = ProjectSerializer(project, many=False)

        return Response(serializer.data)


class ProfilesCRUD:
    @staticmethod
    @api_view(['GET'])
    def get_multi(request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    def get_single(request, pk):
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile, many=False)

        return Response(serializer.data)

