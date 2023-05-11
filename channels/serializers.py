from rest_framework import serializers
from users.models import User


class ChannelViewSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    followings_count = serializers.SerializerMethodField()

    def get_followings_count(self, obj):
        return obj.followings.count()

    class Meta:
        model = User
        fields = ['email', 'username', 'profile_image', 'tags', 'followings_count']
