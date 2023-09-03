from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import ProjectIdea
from projects.permissions import IsOwnerOrReadOnly
from projects.serializers import ProjectIdeaSerializer


class ProjectIdeaAllView(APIView):
    def get(self, request):
        queryset = ProjectIdea.objects.all()
        serializer = ProjectIdeaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ProjectIdeaSerializer(data=data)
        if serializer.is_valid():
            project_idea = ProjectIdea(**serializer.validated_data, owner=request.user)
            project_idea.save()
            serializer = ProjectIdeaSerializer(project_idea)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectIdeaView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, **kwargs):
        try:
            obj = ProjectIdea.objects.get(code=kwargs["code"])
        except (ProjectIdea.DoesNotExist, ValidationError):
            return Response(
                {"message": "Project idea with this ID does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ProjectIdeaSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        owner = request.user
        try:
            obj = ProjectIdea.objects.get(code=kwargs["code"], owner=owner)
        except (ProjectIdea.DoesNotExist, ValidationError):
            return Response(
                {"message": "Project idea with this ID does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        obj.delete()
        return Response({"message": "Project Idea deleted"}, status=status.HTTP_200_OK)
