from rest_framework import serializers
from feeds.models import Feed, Comment
from users.serializers import TagSerializer

#from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#from django.utils.encoding import force_bytes
#from users.tokens import account_activation_token

#from drf_extra_fields.fields import Base64ImageField
# from drf_extra_fields.fields import Base64ImageField

class FeedDetailSerializer(serializers.ModelSerializer): 
    user = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    tag = TagSerializer(many=True)

    """해당 serializer에 추가하거나 프론트로 연결할 기능"""
    # feed작성한 user channel 정보 가져오기
    # tag 게시글에 추가하기
    # 인기 순 혹은 관련된 게시글 목록 가져오기
    class Meta:
        model = Feed
        fields = '__all__'
        extra_kwargs = {'id' : {'read_only' : True},
                        'user' : {'read_only' : True},
                        'created_at' : {'read_only' : True},
                        'updated_at' : {'read_only' : True},
                        }
    
    def get_user(self, obj):
        return obj.user.username  #Feed, author의 username값

    def get_user_id(self, obj):
        return obj.user.id  #Feed, author의 id값

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return 0 #obj.likes.count()


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    def get_likes_count(self, obj):
        return obj.likes.count()
    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "updated_at", "likes", "dislikes", "user",]


class FeedListSerializer(serializers.ModelSerializer):  
    user = serializers.SerializerMethodField()
    tag = TagSerializer(many=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_user(self, obj):
        return obj.user.username  #feed작성한 username값
    
    class Meta:
        model = Feed
        fields = ['id', 'title', 'image', 'user', 'video_key', 'tag', 'likes_count',]
        

class FeedCreateSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)

    class Meta:
        model = Feed
        fields = ["title", 'context','image', 'video_key', 'tag', 'likes',] # 더미데이터 작성을 위해 만들어둠. 나중에 likes 빼기

class FeedSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ["title","context","id",]