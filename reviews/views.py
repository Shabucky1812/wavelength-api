from rest_framework import generics, permissions, serializers, filters
from wavelength.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'score'
    ]
    filterset_fields = [
        'track'
    ]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail':
                 'user has already reviewed this track, '
                 'please edit existing instead'})


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
