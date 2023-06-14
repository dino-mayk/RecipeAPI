from django.db import IntegrityError
from rest_framework import serializers

from apis.models import Ingredient, IngredientName


class IngredientNameSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.CharField(
        max_length=150,
    )

    def create(self, validated_data):
        ingredient_name = IngredientName.objects.create(**validated_data)
        return ingredient_name

    class Meta:
        model = IngredientName
        fields = [
            'id',
            'title',
        ]


class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    ingredient_name = IngredientNameSerializer()

    def create(self, validated_data):

        try:
            ingredient_name = IngredientName.objects.create(
                title=validated_data['ingredient_name']['title'],
            )
        except IntegrityError:
            ingredient_name = IngredientName.objects.filter(
                title=validated_data['ingredient_name']['title'],
            )[0]

        ingredient = Ingredient.objects.create(
            ingredient_name=ingredient_name,
            quantity=validated_data['quantity'],
        )

        return ingredient

    class Meta:
        model = Ingredient
        fields = [
            'ingredient_name',
            'quantity',
        ]
