from django.urls import include, path
from rest_framework import routers

from ingredient.views import IngredientNameViewSet, IngredientViewSet

router = routers.DefaultRouter()

router.register(r'ingredient_name', IngredientNameViewSet)
router.register(r'ingredient', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
