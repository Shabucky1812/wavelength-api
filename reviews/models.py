from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from tracks.models import Track


class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)])
    opinion = models.TextField(max_length=500)
    reviewed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-reviewed_at']

    def __str__(self):
        return self.opinion
