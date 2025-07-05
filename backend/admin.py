from django.contrib import admin
from backend.models.task import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed', 'created', 'modified')
    list_filter = ('completed',)
    search_fields = ('title', 'description')
    ordering = ('-created',)