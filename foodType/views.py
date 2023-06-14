from rest_framework import viewsets

from apis.models import FoodType
from apis.serializers import FoodTypeSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
