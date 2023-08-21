from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model - an instance of this model is created
    automatically for every new user that registers a new
    Wavelength account. Represents the user's visible profile.
    Related to 'owner' - the django User model.
    Instances of the Profile model are ordered by the time they were
    created, with newer instances being listed first.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/', default='../profile_image_pvk7vp'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Create a new Profile instance with the new User as the 'owner'
    field.
    """
    if created:
        Profile.objects.create(owner=instance)


# Calls the create_profile function upon new User creation
post_save.connect(create_profile, sender=User)
