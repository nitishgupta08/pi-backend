from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from silk.profiling.profiler import silk_profile

from projects.models import ProjectIdea
from projects.permissions import IsOwnerOrReadOnly
from projects.serializers import ProjectIdeaSerializer


class ProjectIdeaAllView(APIView):
    def get(self, request):
        queryset = ProjectIdea.objects.select_related("owner").all()
        serializer = ProjectIdeaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectIdeaSerializer(data=request.data)
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
            obj = ProjectIdea.objects.select_related("owner").get(code=kwargs["code"])
        except (ProjectIdea.DoesNotExist, ValidationError):
            return Response(
                {"message": "Project idea with this ID does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ProjectIdeaSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @silk_profile(name="Update Project Idea")
    def patch(self, request, **kwargs):
        try:
            obj = ProjectIdea.objects.get(code=kwargs["code"], owner=request.user)
        except (ProjectIdea.DoesNotExist, ValidationError):
            return Response(
                {"message": "Project idea with this ID does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ProjectIdeaSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        try:
            obj = ProjectIdea.objects.get(code=kwargs["code"], owner=request.user)
        except (ProjectIdea.DoesNotExist, ValidationError):
            return Response(
                {"message": "Project idea with this ID does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        obj.delete()
        return Response({"message": "Project Idea deleted"}, status=status.HTTP_200_OK)
