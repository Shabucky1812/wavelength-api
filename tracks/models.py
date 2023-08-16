from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):

    genre_choices = [
        (0, 'No genre'), (1, 'Pop'), (2, 'Rock'),
        (3, 'Hip-Hop'), (4, 'Country'), (5, 'R&B'),
        (6, 'Folk'), (7, 'Jazz'), (8, 'Metal'),
        (9, 'EDM'), (10, 'Soul'), (11, 'Funk'),
        (12, 'Reggae'), (13, 'Punk'), (14, 'Classical'),
        (15, 'Trap')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    track_ref = models.URLField(blank=True)
    title = models.CharField()
    artist = models.CharField()
    cover_art = models.ImageField(
        upload_to='images/', default='../no_image_found_yzsd7j')
    genre = models.IntegerField(
        choices=genre_choices, default=0
    )
    opinion = models.TextField(blank=True, max_length=500)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} - {self.title}'
