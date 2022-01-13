from django.contrib import admin

from animation.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']