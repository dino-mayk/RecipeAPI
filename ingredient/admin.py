from django.contrib import admin

from ingredient.models import Ingredient, IngredientName


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = [
        'ingredient_name',
    ]


@admin.register(IngredientName)
class AdminIngredientName(admin.ModelAdmin):
    list_display = [
        'title',
    ]
