# Generated by Django 4.2.4 on 2023-09-02 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectShowcase",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("level", models.CharField(choices=[("BEGINNER", "BEGINNER"), ("INTERMEDIATE", "INTERMEDIATE"), ("ADVANCED", "ADVANCED")], max_length=15)),
                ("published", models.DateTimeField(auto_now_add=True)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="URL",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("link", models.URLField()),
                ("title", models.CharField(choices=[("Github", "Github"), ("Live Site", "Live Site")], max_length=20)),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="projects.projectshowcase")),
            ],
        ),
        migrations.AddField(
            model_name="projectshowcase",
            name="tags",
            field=models.ManyToManyField(blank=True, to="projects.tag"),
        ),
        migrations.CreateModel(
            name="ProjectIdea",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("rating", models.FloatField(default=5)),
                ("level", models.CharField(choices=[("BEGINNER", "BEGINNER"), ("INTERMEDIATE", "INTERMEDIATE"), ("ADVANCED", "ADVANCED")], max_length=30)),
                ("published", models.DateTimeField(auto_now_add=True)),
                ("owner", models.ForeignKey(on_delete=models.SET(projects.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
