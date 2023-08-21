from rest_framework import generics, permissions
from wavelength.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    Lists instances of the Follower model and renders a form to
    create a new Follower Instance if the user is logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        """
        Creates an instance of the Follower model using the current
        user as the value for the 'owner' field.
        """
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves and diplays a specific instance of the Follower model
    based on the id value present in the URL.
    If the logged in user is the owner of the displayed instance, the
    view also lets them destroy it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
