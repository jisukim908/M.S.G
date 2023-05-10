from rest_framework import serializers
from feeds.models import Feed, Comment

class FeedDetailSerializer(serializers.ModelSerializer): 
    user = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    """해당 serializer에 추가하거나 프론트로 연결할 기능"""
    # feed작성한 user channel 정보 가져오기
    # tag 게시글에 추가하기
    # 인기 순 혹은 관련된 게시글 목록 가져오기

    #### class Meta가 빠짐! 그래서 추가함
    class Meta:
        model = Feed
        exclude = ("id",)
    
    def get_user(self, obj):
        return obj.user.email  #Feed, author의 email값

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()


class CommentSerializer(serializers.ModelSerializer):
    def get_likes_count(self, obj):
        return obj.likes.count()
    class Meta:
        model = Comment
        fields = ["id", "feed", "text", "created_at", "updated_at", "likes", "dislikes"]


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
        fields = ["title", 'context','image','video',]
        extra_kwargs = {'likes': {'read_only' : True}}
