from rest_framework.generics import RetrieveUpdateDestroyAPIView
from projects.models import ProjectIdea
from projects.serializers import ProjectIdeaSerializer
from projects.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProjectIdeaAllView(APIView):
    def get(self, request):
        queryset = ProjectIdea.objects.select_related("owner").all()
        serializer = ProjectIdeaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectIdeaView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ProjectIdea.objects.all()
    serializer_class = ProjectIdeaSerializer
