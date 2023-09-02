from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import Tag, ProjectShowcase, ProjectIdea, URL
from django.utils import timezone

# Register your models here.

admin.site.register(Tag)
admin.site.register(ProjectIdea)
admin.site.register(ProjectShowcase)
admin.site.register(URL)


# @admin.register(ProjectIdea)
# class ProjectIdeaAdmin(admin.ModelAdmin):
#     resource_class = TodoResource
#     list_display = ["title", "status", "due_date", "created_at", "owner"]
#     ordering = ["due_date"]
#     readonly_fields = ("created_at",)
#     search_fields = ("title__startswith",)
#     search_help_text = "Search by title"
#     filter_horizontal = ("tags",)
#     radio_fields = {"status": admin.HORIZONTAL}
#     fieldsets = [
#         ("Mandatory Fields", {"fields": ["owner", ("title", "due_date"), "status"]}),
#         ("Optional Fields", {"fields": ["description", "tags"]}),
#         ("Created At", {"fields": ["created_at"]}),
#     ]
#     list_filter = ["status", "tags"]
#
#     actions = ["status_done"]
#
#     @admin.action(description="Update status of selected as DONE")
#     def status_done(self, request, queryset):
#         """
#         Added action that allows user to mark multiple tasks as done
#         """
#         updated = queryset.update(status="DONE")
#         self.message_user(
#             request,
#             ngettext(
#                 "%d story was successfully marked as published.",
#                 "%d stories were successfully marked as published.",
#                 updated,
#             )
#             % updated,
#             messages.SUCCESS,
#         )


admin.site.site_header = "Projects Share Administration"
admin.site.site_title = "Projects Share Administration"
admin.site.index_title = "Project Share Admin"
