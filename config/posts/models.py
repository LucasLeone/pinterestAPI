# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model.
    
    The post has a title, text, photo,
    user and extra info.
    """

    title = models.CharField(max_length=250)
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='posts/photos/')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return post id and username."""
        return f'{self.user.username}: {self.pk}'