"""Rest endpoints for User and Token related stuff
"""
# Django REST Framework
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

# First Party
from core.models import Category, Item
from sharejoy.serializers import (
    AuthTokenSerializer,
    CategorySerializer,
    ItemSerializer,
    UserSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create new user"""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create new auth token for user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ItemViewSet(
    viewsets.GenericViewSet,
    generics.RetrieveUpdateDestroyAPIView,
    generics.ListAPIView,
    generics.CreateAPIView,
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryViewSet(
    viewsets.GenericViewSet,
    generics.RetrieveUpdateDestroyAPIView,
    generics.ListAPIView,
    generics.CreateAPIView,
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
