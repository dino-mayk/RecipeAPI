from django.urls import include, path
from rest_framework import routers

from foodType.views import FoodTypeViewSet

router = routers.SimpleRouter()

router.register(r'food_type', FoodTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
