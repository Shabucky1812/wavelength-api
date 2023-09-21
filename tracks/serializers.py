from rest_framework import serializers
from tracks.models import Track
from reviews.models import Review
from django.contrib.humanize.templatetags.humanize import naturaltime


class TrackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Track model.
    Edits the 'owner' field to the username value of the User instance
    that it represents for better readability.
    Creates the 'is_owner' field to determine whether the logged in user is
    the owner of the Track instance.
    Creates the 'profile_id' and 'profile_image' fields to display basic
    information about the user sharing the track.
    Creates the 'average_score' field to display the average score for
    the track based on it's reviews.
    Receives the 'reviews_count' field from the view to display how many
    reviews the track has received.
    Creates the 'review_id' field to display the review for the track
    created by the current user, if one exists.
    Updates the 'created_at' field to a natural time format.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    genre = serializers.ReadOnlyField(source='get_genre_id_display')
    average_score = serializers.SerializerMethodField()
    reviews_count = serializers.ReadOnlyField()
    review_id = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def validate_cover_art(self, value):
        """
        Prevents users from uploading large images to the site, ensuring better
        performance.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        return value

    def get_is_owner(self, obj):
        """
        Determines if the current user is the owner of the Track
        instance.
        returns True or False depending on if the current user is or
        is not the owner.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_average_score(self, obj):
        """
        Receives all reviews for a track and uses the 'score' value of
        each to determine the Track's average score.
        returns None if no reviews for the track exist yet.
        returns the calculated average score value if the track has been
        reviewed.
        """
        track_reviews = Review.objects.filter(track=obj.id)
        if track_reviews:
            scores = []
            for review in track_reviews:
                scores.append(review.score)
            return round(sum(scores) / len(scores))
        return None

    def get_review_id(self, obj):
        """
        Determines if the current user has reviewed this Track and
        receives the id of the relevant Review instance if they have.
        returns None if the user is not logged in/hasn't reviewed the Track.
        returns the id of the relevant Review instance if the current user
        has reviewed Track.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(
                owner=user, track=obj
            ).first()
            return review.id if review else None
        return None

    def get_created_at(self, obj):
        """
        Reformats the 'created_at' DateTime value into a more
        readable natural time format.
        """
        return naturaltime(obj.created_at)

    class Meta:
        model = Track
        fields = [
            'id', 'owner', 'title', 'artist', 'cover_art', 'genre_id',
            'genre', 'opinion', 'is_owner', 'profile_id', 'profile_image',
            'average_score', 'reviews_count', 'review_id', 'created_at'
        ]
