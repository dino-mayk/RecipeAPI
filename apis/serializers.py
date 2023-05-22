from rest_framework import serializers

from apis.models import Recipe


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
