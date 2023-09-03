from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import ProjectIdea


class ProjectIdeaSerializer(ModelSerializer):
    owner = SerializerMethodField()

    def get_owner(self, obj):
        return obj.owner.username

    class Meta:
        model = ProjectIdea
        fields = ["title", "content", "rating", "level", "published", "owner"]
