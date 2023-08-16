from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Track
from .serializers import TrackSerializer


class TrackList(APIView):
    def get(self, request):
        tracks = Track.objects.all()
        serializer = TrackSerializer(
            tracks, many=True, context={'request': request})
        return Response(serializer.data)
