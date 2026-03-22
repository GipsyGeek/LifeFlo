from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BloodDriveViewSet, DonorProfileViewSet

router = DefaultRouter()
router.register(r'drives', BloodDriveViewSet)
router.register(r'donors', DonorProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]