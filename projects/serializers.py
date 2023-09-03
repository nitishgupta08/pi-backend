from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    DateTimeField,
    ValidationError,
)
from .models import ProjectIdea


class ProjectIdeaSerializer(ModelSerializer):
    owner = SerializerMethodField()
    published = DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    def get_owner(self, obj):
        return obj.owner.username

    class Meta:
        model = ProjectIdea
        fields = ["code", "title", "content", "rating", "level", "published", "owner"]

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise ValidationError("Rating must be between 0 and 5.")
        return value
