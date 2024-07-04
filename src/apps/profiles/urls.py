from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProfileViewSet

router = SimpleRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
