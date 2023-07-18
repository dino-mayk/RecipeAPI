from django.contrib import admin

from recipe.models import Recipe, RecipeImage


@admin.register(RecipeImage)
class AdminRecipeImage(admin.ModelAdmin):
    list_display = [
        'id',
    ]


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = [
        'title',
    ]
