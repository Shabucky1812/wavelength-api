from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from wavelength.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        tracks_count=Count('owner__track', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
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


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        tracks_count=Count('owner__track', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
