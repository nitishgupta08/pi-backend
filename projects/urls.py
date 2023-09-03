from django.urls import path
from projects.views.project_idea.views import ProjectIdeaAllView, ProjectIdeaView

urlpatterns = [
    path("project-ideas/", ProjectIdeaAllView.as_view()),
    path("project-ideas/<int:pk>/", ProjectIdeaView.as_view()),
]
