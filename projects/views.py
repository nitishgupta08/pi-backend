from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProjectIdea
from .serializers import ProjectIdeaSerializer
from .permissions import IsOwnerOrReadOnly


class ProjectIdeaAllView(ListCreateAPIView):
    queryset = ProjectIdea.objects.all()
    serializer_class = ProjectIdeaSerializer


class ProjectIdeaView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = ProjectIdea.objects.all()
    serializer_class = ProjectIdeaSerializer
