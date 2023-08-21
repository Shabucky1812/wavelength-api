from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from wavelength.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ProfileList(generics.ListAPIView):
    """
    Lists the instances of the Profile modeland orders them by
    time created with newer instances appearing first.
    Adds ordering_fields to let users order by the following fields:
    tracks_count, followers_count, following_count, as well as by how
    long users have been following a given account, and by how long
    users have been followed by a given account.
    Also lets the user search profiles by the owner's username and
    filter by users that are either following a given account or are
    followed by a given account.
    """
    queryset = Profile.objects.annotate(
        tracks_count=Count('owner__track', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'tracks_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    search_fields = [
        'owner__username'
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieves an displays a specific instance of the Profile model
    based on the id value present in the URL. If the current user is
    the owner of the Profile, an update form is rendered that allows
    the user to update their profile image.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        tracks_count=Count('owner__track', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
