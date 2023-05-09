from rest_framework import serializers
from .models import Feed, Comment

<<<<<<< HEAD
class FeedDetailSerializer(serializers.ModelSerializer): 
    user = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    """해당 serializer에 추가하거나 프론트로 연결할 기능"""
    # feed작성한 user channel 정보 가져와기
    # 인기 순 혹은 관련된 게시글 목록 가져오기

    
    def get_user(self, obj):
        return obj.user.email  #Feed, author의 email값

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Feed
        fields = ['title','context', 'image','video', 'created_at', 'updated_at', 'user', "comments_count", "likes_count",]


class FeedListSerializer(serializers.ModelSerializer):  
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username  #feed작성한 username값

    class Meta:
        model = Feed
        fields = ['title', 'image', 'user',]

class FeedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['title','context', 'image','video',]

=======

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
>>>>>>> b7c59d0 (댓글 생성,수정,삭제 / 피드 생성,수정,삭제)
