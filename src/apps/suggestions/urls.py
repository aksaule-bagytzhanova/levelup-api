from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StarViewSet, SuggestionViewSet, RecommendationViewSet

router = DefaultRouter()
router.register(r'suggestions', SuggestionViewSet, basename='suggestion')
router.register(r'recommendations', RecommendationViewSet, basename='recommendation')
router.register(r'stars', StarViewSet, basename='star')

urlpatterns = [
    path('', include(router.urls)),
]
