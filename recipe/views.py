from rest_framework import viewsets

from recipe.models import Recipe, RecipeImage
from recipe.serializers import RecipeImageSerializer, RecipeSerializer


class RecipeImageViewSet(viewsets.ModelViewSet):
    queryset = RecipeImage.objects.all()
    serializer_class = RecipeImageSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
