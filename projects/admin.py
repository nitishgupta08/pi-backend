from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Tag, ProjectShowcase, ProjectIdea, URL
from django.utils import timezone

admin.site.register(Tag)


class URLInline(admin.TabularInline):
    model = URL
    extra = 1


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ["project", "website"]
    list_filter = ["website"]


@admin.register(ProjectIdea)
class ProjectIdeaAdmin(admin.ModelAdmin):
    readonly_fields = ("code", "published")
    list_display = ["title", "owner", "level", "rating", "published"]
    ordering = ["published"]

    fieldsets = [
        ("Owner", {"fields": ["owner"]}),
        ("Content Fields", {"fields": ["title", "content"]}),
        ("Rating Fields", {"fields": ["level", "rating"]}),
        ("ReadOnly Fields", {"classes": ["collapse"], "fields": ["code", "published"]}),
    ]

    search_fields = ("title__startswith",)
    search_help_text = "Search by title"
    list_filter = ["level"]


@admin.register(ProjectShowcase)
class ProjectShowcaseAdmin(admin.ModelAdmin):
    readonly_fields = ("code", "published")
    list_display = ["title", "owner", "level", "published"]
    ordering = ["published"]

    fieldsets = [
        ("Owner", {"fields": ["owner"]}),
        ("Content Fields", {"fields": ["title", "content", "tags"]}),
        ("Rating Fields", {"fields": ["level"]}),
        ("ReadOnly Fields", {"classes": ["collapse"], "fields": ["code", "published"]}),
    ]

    search_fields = ("title__startswith",)
    search_help_text = "Search by title"
    list_filter = ["level"]
    filter_horizontal = ("tags",)
    inlines = [URLInline]


admin.site.site_header = "Projects Share Administration"
admin.site.site_title = "Projects Share Administration"
admin.site.index_title = "Project Share Admin"
