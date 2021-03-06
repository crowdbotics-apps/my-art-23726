from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    CountryViewSet,
    ItemViewSet,
    ItemVariantViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register("country", CountryViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("review", ReviewViewSet)
router.register("category", CategoryViewSet)
router.register("item", ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
