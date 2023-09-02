from rest_framework import generics, permissions, filters
from .models import Track
from .serializers import TrackSerializer
from wavelength.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class TrackList(generics.ListCreateAPIView):
    """
    Lists the instances of the Track model and renders a form to
    create a new Track instance if the user is logged in.
    Also allows the user to order the tracks by the total number
    of reviews per track, and how recently the tracks were last
    reviewed. Lets the user search the tracks by: owner's username,
    track title, and track artist. Additionally, lets the user filter
    the tracks by: genre, owner, and by who has reviewed them.
    """
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.annotate(
        reviews_count=Count('review', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'reviews_count',
        'review__reviewed_at'
    ]
    search_fields = [
        'owner__username',
        'title',
        'artist'
    ]
    filterset_fields = [
        'genre_id',
        'owner__profile',
        'review__owner__profile'
    ]

    def perform_create(self, serializer):
        """
        Creates an instance of the Track model using the current
        user as the value for the 'owner' field.
        """
        serializer.save(owner=self.request.user)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves an displays a specific instance of the Track model
    based on the id value present in the URL. If the current user is
    the owner of the Track than a form is rendered to update the
    track, and a delete button is rendered allowing them to destroy
    the instance.
    """
    serializer_class = TrackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Track.objects.annotate(
        reviews_count=Count('review', distinct=True),
    ).order_by('-created_at')
