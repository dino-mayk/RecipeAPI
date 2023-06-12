from django.urls import include, path
from rest_framework import routers

from apis.views import (
    FoodTypeViewSet,
    IngredientNameViewSet,
    IngredientViewSet,
    RecipeImageViewSet,
    RecipeViewSet,
)

router = routers.DefaultRouter()

router.register(r'ingredient_name', IngredientNameViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'food_type', FoodTypeViewSet)
router.register(r'recipe_image', RecipeImageViewSet)
router.register(r'recipe', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
