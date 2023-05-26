from rest_framework import serializers, status
from rest_framework.response import Response

from apis.models import FoodType, Ingredient, IngredientName, Recipe


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.CharField(
        max_length=150,
    )

    class Meta:
        model = FoodType
        fields = [
            'id',
            'title',
        ]


class IngredientNameSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.CharField(
        max_length=150,
    )

    class Meta:
        model = IngredientName
        fields = [
            'id',
            'title',
        ]


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    title = IngredientNameSerializer()

    class Meta:
        model = Ingredient
        fields = [
            'title',
            'quantity',
        ]


class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.CharField(
        max_length=150,
    )
    food_type = FoodTypeSerializer()
    ingredients = IngredientSerializer(many=True)

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

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
