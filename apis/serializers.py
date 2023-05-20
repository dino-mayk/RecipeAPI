from rest_framework import serializers

from apis.models import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'photo',
            'ingredients',
            'cooking_time',
            'title',
            'description',
            'food_type',
            'created_on',
        ]
