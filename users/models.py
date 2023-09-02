from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="data/profile_image", blank=True, null=True)
    bio = models.TextField(max_length=512, blank=True, null=True)
