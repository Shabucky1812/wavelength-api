from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    """
    Track model - represents one instance of a shared track.
    Related to 'owner' - the django User model.
    Instances of the Track model are ordered by the time they were
    created, with newer instances being listed first.
    """
    # available genre choices for the 'genre' field
    genre_choices = [
        (0, 'No genre'), (1, 'Pop'), (2, 'Rock'),
        (3, 'Hip-Hop'), (4, 'Country'), (5, 'R&B'),
        (6, 'Folk'), (7, 'Jazz'), (8, 'Metal'),
        (9, 'EDM'), (10, 'Soul'), (11, 'Funk'),
        (12, 'Reggae'), (13, 'Punk'), (14, 'Classical'),
        (15, 'Trap')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    cover_art = models.ImageField(
        upload_to='images/', default='../no_image_found_yzsd7j')
    genre_id = models.IntegerField(
        choices=genre_choices, default=0
    )
    opinion = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} - {self.title}'
