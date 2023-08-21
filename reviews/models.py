from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from tracks.models import Track


class Review(models.Model):
    """
    Review model - represents a single review for a track.
    Related to 'owner' - the django User model - and 'track' -
    the Track instance the review is intended for. Instances of
    the Review model are ordered by the time the review was created/
    last updated with newer/more recently updated review appearing
    first. The unique_together constraint is also applied to
    prevent one user from creating multiple reviews of one track.
    This is intended to prevent or at least decrease review bombing.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)])
    opinion = models.TextField(max_length=500)
    reviewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reviewed_at']
        unique_together = ['owner', 'track']

    def __str__(self):
        return self.opinion
