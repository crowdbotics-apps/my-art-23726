from rest_framework import authentication
from menu.models import Category, Country, Item, ItemVariant, Review
from .serializers import (
    CategorySerializer,
    CountrySerializer,
    ItemSerializer,
    ItemVariantSerializer,
    ReviewSerializer,
)
from rest_framework import viewsets


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Country.objects.all()


class ItemVariantViewSet(viewsets.ModelViewSet):
    serializer_class = ItemVariantSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ItemVariant.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Review.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Item.objects.all()
