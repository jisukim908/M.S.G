from rest_framework import serializers
from .models import Feed, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "feed", "text", "created_at", "updated_at", "likes", "dislikes"]


class FeedSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Feed
        fields = [
            "id",
            "title",
            "content",
            "image",
            "video",
            "created_at",
            "updated_at",
            "likes",
            "comments",
            "likes_count",
        ]
        read_only_fields = ["likes", "comments", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()
