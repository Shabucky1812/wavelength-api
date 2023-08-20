from rest_framework import generics, permissions, filters
from .models import Track
from .serializers import TrackSerializer
from wavelength.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class TrackList(generics.ListCreateAPIView):
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
        'genre',
        'owner__profile',
        'review__owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Track.objects.annotate(
        reviews_count=Count('review', distinct=True),
    ).order_by('-created_at')
