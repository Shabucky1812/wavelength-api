from rest_framework import generics, permissions
from .models import Track
from .serializers import TrackSerializer
from wavelength.permissions import IsOwnerOrReadOnly


class TrackList(generics.ListCreateAPIView):
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Track.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TrackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Track.objects.all()
