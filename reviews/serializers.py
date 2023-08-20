from rest_framework import serializers
from .models import Review
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reviewed_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_reviewed_at(self, obj):
        return naturaltime(obj.reviewed_at)

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'track', 'score', 'opinion', 'reviewed_at',
            'is_owner', 'profile_id', 'profile_image'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    track = serializers.ReadOnlyField(source="track.id")
