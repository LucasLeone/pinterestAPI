# Django
from django.contrib.auth import get_user_model

# Django REST Framework
from rest_framework import viewsets

# Serializers
from posts.serializers import PostSerializer, UserSerializer

# Permissions
from posts.permissions import IsOwnerOrReadOnly

# Model
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    """Post viewset."""

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """User viewset."""

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
