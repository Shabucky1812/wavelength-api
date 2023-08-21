from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model - represents one instance of a user following
    another user. Related to 'owner' - the user doing the following -
    and 'followed' - the user being followed by 'owner'. These fields
    both have related_name values to differentiate between them, as they
    are both related to the Django User model.
    Instances of the Follower model are ordered by the time they were
    created, with newer instances being listed first.
    The unique_together constraint is also applied to prevent users from
    following the same user more than once.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} - {self.followed}'
