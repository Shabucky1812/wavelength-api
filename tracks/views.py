from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.http import Http404
from .models import Track
from .serializers import TrackSerializer
from wavelength.permissions import IsOwnerOrReadOnly


class TrackList(APIView):
    serializer_class = TrackSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        tracks = Track.objects.all()
        serializer = TrackSerializer(
            tracks, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TrackSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class TrackDetail(APIView):
    serializer_class = TrackSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            track = Track.objects.get(id=id)
            self.check_object_permissions(self.request, track)
            return track
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, id):
        track = self.get_object(id)
        serializer = TrackSerializer(track, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        track = self.get_object(id)
        serializer = TrackSerializer(
            track, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        track = self.get_object(id)
        track.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
