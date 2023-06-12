from django.contrib import admin

from apis.models import (FoodType, Ingredient, IngredientName, Recipe,
                         RecipeImage)


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(RecipeImage)
class AdminRecipeImage(admin.ModelAdmin):
    list_display = [
        'id',
    ]


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


@admin.register(FoodType)
class AdminFoodType(admin.ModelAdmin):
    list_display = [
        'title',
    ]
