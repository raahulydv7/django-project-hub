from django.contrib import admin
from .models import CustomUser,Profile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','role','created_at']
    search_fields = ['username','email']
    ordering = ['-created_at']
    list_filter = ['role','created_at']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_username', 'created_at']
    search_fields = ['user__username']
    ordering = ['-created_at']
    list_filter = ['created_at']

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'