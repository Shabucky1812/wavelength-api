from rest_framework import serializers
from .models import Review
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    Edits the 'owner' field to the username value of the User instance
    that it represents for better readability.
    Creates the 'is_owner' field to determine whether the logged in user is
    the owner of the Review instance.
    Creates the 'profile_id' and 'profile_image' fields to display basic
    information about the user leaving the review.
    Also edits the 'reviewed_at' field to a natural time format.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reviewed_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Determines if the current user is the owner of the Review
        instance.
        returns True or False depending on if the current user is or
        is not the owner.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_reviewed_at(self, obj):
        """
        Reformats the 'reviewed_at' DateTime value into a more
        readable natural time format.
        """
        return naturaltime(obj.reviewed_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'track', 'score', 'opinion', 'reviewed_at',
            'is_owner', 'profile_id', 'profile_image'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Inherits from the ReviewSerializer class.
    Additionally updates the 'track' field to the specific
    track in the detail view.
    """
    track = serializers.ReadOnlyField(source="track.id")
