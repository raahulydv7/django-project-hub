from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'manager', 'status', 'created_at']
    search_fields = ['title', 'manager__username']
    list_filter = ['status', 'created_at']