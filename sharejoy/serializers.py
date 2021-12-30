"""Serializers for User and Token models
"""
# Builtins
from typing import Any, Dict

# Django
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _

# Django REST Framework
from rest_framework import serializers

# First Party
from core.models import Category, Item


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User object"""

    class Meta:
        """User's serializer meta"""

        model = get_user_model()
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True, "min_length": 10}}

    def create(self, validated_data: Dict[str, str]) -> Any:
        """Create user and encrypt the password

        Args:
            validated_data (Dict[str, str]): Username, email, password etc.

        Returns:
            User: Created user with encrypted password
        """
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance: Any, validated_data: Dict[str, str]) -> Any:
        """Update user and ensure the new password has also been encrypted

        Args:
            instance (Any): Model instance before
            validated_data (Dict[str, str]): Payload data

        Returns:
            Any: Updated user with encrypted password
        """
        password = validated_data.pop("password", None)
        user = super().update(instance=instance, validated_data=validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the AuthToken object"""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs: Any) -> Any:
        """Authenticate user

        Args:
            attrs (Any): Request payload

        Returns:
            Any: User with token
        """
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user

        return attrs


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""

    class Meta:
        """Category's Meta"""

        model = Category
        fields = "__all__"
        read_only_fields = ("id",)


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for Item model"""

    class Meta:
        """Item's Meta"""

        model = Item
        fields = "__all__"
        read_only_fields = ("id",)
