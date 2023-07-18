from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from foodType.models import FoodType
from foodType.serializers import FoodTypeSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('title', )
