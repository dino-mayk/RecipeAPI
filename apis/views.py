from rest_framework import viewsets

from apis.models import FoodType, Ingredient, IngredientName, Recipe
from apis.serializers import (FoodTypeSerializer, IngredientNameSerializer,
                              IngredientSerializer, RecipeSerializer)


class IngredientNameViewSet(viewsets.ModelViewSet):
    queryset = IngredientName.objects.all()
    serializer_class = IngredientNameSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
