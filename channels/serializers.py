from rest_framework import serializers
from users.models import User


class ChannelViewSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'profile_image', 'tags', 'followings']
