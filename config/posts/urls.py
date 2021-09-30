# Django
from django.urls import path

# Django REST Framework
from rest_framework.routers import SimpleRouter

# Views
from posts.views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls