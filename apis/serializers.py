from rest_framework import serializers

from apis.models import Ingredient, FoodType, Recipe


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'title']


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):

    def to_representation(self):
        return id

    def __str__(self):
        return title

    class Meta:
        model = FoodType
        fields = ['id', 'title']


class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'id',
            'food_type',
            'ingredients',
            'photo',
            'cooking_time',
            'title',
            'description',
        ]
