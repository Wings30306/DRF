from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Create your models here.
class Like(models.Model):
    """
    Like model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'UniqueConstraint' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        models.UniqueConstraint(fields=["owner", "post"], name="unique_like")

    def __str__(self):
        return f"Post {self.post} liked by {self.owner}"
