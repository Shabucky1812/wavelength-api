from rest_framework import generics, permissions
from wavelength.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django.db import IntegrityError


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise IntegrityError(
                'You have already reviewed this track, '
                'please edit your existing review instead.')


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
