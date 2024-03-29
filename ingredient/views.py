from rest_framework import viewsets

from ingredient.models import Ingredient, IngredientName
from ingredient.serializers import (IngredientNameSerializer,
                                    IngredientSerializer)


class IngredientNameViewSet(viewsets.ModelViewSet):
    queryset = IngredientName.objects.all()
    serializer_class = IngredientNameSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
