from rest_framework import serializers

from apis.models import IngredientName, Ingredient, FoodType, Recipe


class IngredientNameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IngredientName
        fields = ['id', 'title']


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'title', 'quantity']


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):

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
