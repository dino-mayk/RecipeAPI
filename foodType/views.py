from rest_framework import viewsets

from foodType.models import FoodType
from foodType.serializers import FoodTypeSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
