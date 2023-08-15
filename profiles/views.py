from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    def get_object(self, id):
        try:
            profile = Profile.objects.get(id=id)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, id):
        profile = self.get_object(id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
