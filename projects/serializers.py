from rest_framework.serializers import ModelSerializer
from .models import ProjectIdea


class ProjectIdeaSerializer(ModelSerializer):
    class Meta:
        model = ProjectIdea
        fields = '__all__'
