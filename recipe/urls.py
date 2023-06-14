from django.urls import include, path
from rest_framework import routers

from recipe.views import RecipeImageViewSet, RecipeViewSet

router = routers.DefaultRouter()

router.register(r'recipe_image', RecipeImageViewSet)
router.register(r'recipe', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
