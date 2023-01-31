from django.contrib import admin

from to_do.models import Tag, Task

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "deadline_time", "is_done"]
    search_fields = ["content", "tags"]
    list_filter = ("is_done",)
