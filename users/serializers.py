from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User
from .models import Profile


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        password = validated_data.pop("password", None)
        if password is not None:
            instance.set_password(password)
            instance.save()

        return instance


class ProfileSerializer(ModelSerializer):
    user = SerializerMethodField()

    def get_user(self, obj):
        user = User.objects.get(profile=obj)

        return {"username": user.username, "email": user.email, "name": user.get_full_name(), "date_joined": user.date_joined, "staff": user.is_staff}

    class Meta:
        model = Profile
        fields = ["user", "profile_image", "bio"]
