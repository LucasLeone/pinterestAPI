# Django
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import serializers

# Models
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post model serializer."""

    user = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())

    class Meta:
        """Meta class."""
        fields = ('id', 'user', 'title', 'text', 'photo')
        model = Post


class UserSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""
        model = get_user_model()
        fields = ('id', 'username')
