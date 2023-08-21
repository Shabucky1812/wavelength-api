from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    Edits the 'owner' field to the username value of the User instance
    that it represents for better readability.
    Creates the 'is_owner' field to determine whether the logged in user is
    the owner of the Profile instance.
    Creates the 'following_id' field to determine if the current user is
    following the Profile and displays the id of the relevant Follower
    instance if so.
    Also receives the 'tracks_count', 'followers_count', and 'following_count'
    fields from the view to display: how many tracks the owner has shared,
    how many followers the owner has, and how many profiles the user is
    following.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    tracks_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Determines if the current user is the owner of the Profile
        instance.
        returns True or False depending on if the current user is or
        is not the owner.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Determines if the current user is following this Profile and
        receives the id of the relevant Follower instance if they are.
        returns None if the user is not logged in/not following the
        Profile. returns the id of the relevant Follower instance if
        the current user is following the owner of the Profile instance,
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile

        fields = [
            'id', 'owner', 'created_at', 'image', 'is_owner', 'following_id',
            'tracks_count', 'followers_count', 'following_count'
        ]
