from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to owner and followed,
    both of which are User instances.
    unique_together makes sure a user can't follow the same user twice.
    # Additional challenge to self if not covered:
    # Make sure a user can't follow themselves.
    """
    owner = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
        )
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f"{self.owner} followed {self.followed}"
