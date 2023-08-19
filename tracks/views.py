from rest_framework import generics, permissions, filters
from .models import Track
from .serializers import TrackSerializer
from wavelength.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class TrackList(generics.ListCreateAPIView):
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.annotate(
        reviews_count=Count('review', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'reviews_count',
        'review__reviewed_at'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Track.objects.annotate(
        reviews_count=Count('review', distinct=True),
    ).order_by('-created_at')
