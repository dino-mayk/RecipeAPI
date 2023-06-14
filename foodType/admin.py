from django.contrib import admin

from foodType.models import FoodType


@admin.register(FoodType)
class AdminFoodType(admin.ModelAdmin):
    list_display = [
        'title',
    ]
