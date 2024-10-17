from django.contrib import admin
from .models import Task

def mark_as_done(modeladmin, request, queryset):
    queryset.update(done=True)
mark_as_done.short_description = "Mark selected tasks as done"
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "done", "created_date", "pk", "creator"]
    actions = [mark_as_done]
