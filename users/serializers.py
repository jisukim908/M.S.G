from rest_framework import serializers
from users.models import User, Tag
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'id']
    
    def __str__(self):
        return self.name

class UserViewSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'profile_image', 'bio', 'joined_at', 'tags', 'followings']

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    
# 회원가입
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'profile_image', 'bio', 'joined_at', 'tags', 'followings']

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairView):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['password'] = user.password
        return token
    
