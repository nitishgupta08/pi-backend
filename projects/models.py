import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LEVEL_CHOICES = (
    ("BEGINNER", "BEGINNER"),
    ("INTERMEDIATE", "INTERMEDIATE"),
    ("ADVANCED", "ADVANCED"),
)


def get_sentinel_user():
    return User.objects.get_or_create(username="deleted")[0]


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return str(f"{self.name}")


class ProjectIdea(models.Model):
    """
    Here rating and level can be altered by other users based on comments
    Even if user is deleted, Project Ideas shouldn't leave website
    """

    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.FloatField(default=5)
    level = models.CharField(max_length=30, choices=LEVEL_CHOICES)
    published = models.DateTimeField(auto_now_add=True)
    code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.title}"


class ProjectShowcase(models.Model):
    # Here if user is deleted, it makes sense to delete all their showcases
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES)
    published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    code = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.title}"


class URL(models.Model):
    LINK_CHOICES = (("Github", "Github"), ("Live Site", "Live Site"))
    project = models.ForeignKey(
        ProjectShowcase, on_delete=models.CASCADE, related_name="url"
    )
    link = models.URLField()
    website = models.CharField(max_length=20, choices=LINK_CHOICES)

    def __str__(self):
        return f"{self.project} | {self.website}"
