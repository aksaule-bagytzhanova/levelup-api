from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuggestionViewSet, RecommendationViewSet

router = DefaultRouter()
router.register(r'suggestions', SuggestionViewSet, basename='suggestion')
router.register(r'recommendations', RecommendationViewSet, basename='recommendation')

urlpatterns = [
    path('', include(router.urls)),
]
