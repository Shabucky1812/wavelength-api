from rest_framework import serializers
from tracks.models import Track
from reviews.models import Review


class TrackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    average_score = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_average_score(self, obj):
        track_reviews = Review.objects.filter(track=obj.id)
        if track_reviews:
            scores = []
            for review in track_reviews:
                scores.append(review.score)
            return round(sum(scores) / len(scores))
        return None

    def get_reviews_count(self, obj):
        track_reviews = Review.objects.filter(track=obj.id)
        if track_reviews:
            return len(track_reviews)
        return 0

    class Meta:
        model = Track
        fields = [
            'id', 'owner', 'track_ref', 'title', 'artist', 'cover_art',
            'genre', 'opinion', 'is_owner', 'profile_id', 'profile_image',
            'average_score', 'reviews_count'
        ]
