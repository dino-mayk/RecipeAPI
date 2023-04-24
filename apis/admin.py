from django.contrib import admin

from apis.models import Recipe


@admin.register(Recipe)
class AdminRecipes(admin.ModelAdmin):
    list_display = [
        'title',
    ]
