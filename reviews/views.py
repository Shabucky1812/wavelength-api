from rest_framework import generics, permissions, serializers, filters
from wavelength.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend


class ReviewList(generics.ListCreateAPIView):
    """
    Lists the instances of the Review model and renders a form to
    create a new Review instance if the user is logged in.
    Also allows the user to order the listed reviews by score and
    to filter them by track.
    """
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
        """
        Checks for an IntegrityError upon attempted creation of
        a new Review instance. This would be raised if the user
        attempting to create the review has already reviewed the
        track.
        If no error is raised, the instance is saved as normal.
        If an error is raised, a message detailing the error is
        passed to the user.
        """
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail':
                 'user has already reviewed this track, '
                 'please edit existing instead'})


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves an displays a specific instance of the Review model
    based on the id value present in the URL. If the current user is
    the owner of the Review than a form is rendered to update the
    review, and a delete button is rendered allowing them to destroy
    the instance.
    """
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.all()
