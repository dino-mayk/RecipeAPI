from django.contrib import admin

from apis.models import FoodType, Ingredient, Recipe


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(FoodType)
class AdminFoodType(admin.ModelAdmin):
    list_display = [
        'title',
    ]
