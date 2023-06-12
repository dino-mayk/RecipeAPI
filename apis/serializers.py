from django.db import IntegrityError
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apis.models import (
    FoodType,
    Ingredient,
    IngredientName,
    Recipe,
    RecipeImage,
)


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.CharField(
        max_length=150,
    )

    def create(self, validated_data):
        food_type = FoodType.objects.create(**validated_data)
        return food_type

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


class RecipeImageSerializer(serializers.HyperlinkedModelSerializer):

    image = Base64ImageField()

    def create(self, validated_data):
        recipe_image = RecipeImage.objects.create(**validated_data)
        return recipe_image

    class Meta:
        model = RecipeImage
        fields = [
            'id',
            'image',
        ]


class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    food_type = FoodTypeSerializer()
    ingredients = IngredientSerializer(
        many=True,
    )
    images = RecipeImageSerializer(
        many=True,
        required=False,
    )
    title = serializers.CharField(
        max_length=150,
    )

    def create(self, validated_data):

        try:
            food_type = FoodType.objects.create(
                title=validated_data['food_type']['title'],
            )
        except IntegrityError:
            food_type = FoodType.objects.filter(
                title=validated_data['food_type']['title'],
            )[0]

        recipe = Recipe.objects.create(
            food_type=food_type,
            cooking_time=validated_data['cooking_time'],
            title=validated_data['title'],
            description=validated_data['description'],
        )

        ingredients = validated_data['ingredients']
        images = validated_data['images']

        for ingredient in ingredients:

            title = ingredient['ingredient_name']['title']
            quantity = ingredient['quantity']

            try:
                ingredient_name = IngredientName.objects.create(
                    title=title,
                )
            except IntegrityError:
                ingredient_name = IngredientName.objects.filter(
                    title=title,
                )[0]

            ingredient = Ingredient.objects.create(
                ingredient_name=ingredient_name,
                quantity=quantity,
            )

            recipe.ingredients.add(ingredient)

        for image in images:

            print(image)
            print('fffffffffffffffffffffffffffffffffffffffffffff')

            recipe_image = RecipeImage.objects.create(
                image=image['image'],
            )

            recipe.images.add(recipe_image)

        return recipe

    class Meta:
        model = Recipe
        fields = [
            'id',
            'food_type',
            'ingredients',
            'images',
            'cooking_time',
            'title',
            'description',
        ]
