from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from rest_framework import status
from users.serializers import (
    MyTokenObtainPairSerializer, UserSerializer, TagSerializer, UserViewSerializer
)
from users.models import Tag, User

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class FollowView(APIView):
    def post(self, request, user_id):
        author = get_object_or_404(User, pk=user_id)
        user = request.user
        if user in author.followings.all():
            author.followings.remove(user)
            return Response({"message":"팔로우 취소"}, status=status.HTTP_200_OK)
        else:
            author.followings.add(user)
            return Response({"message":"팔로우"}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serializer = UserViewSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, user_id):
        """회원 정보를 수정합니다"""
        user = get_object_or_404(User, pk=user_id)
        print(user, type(user))
        print(request.user, type(request.user))
        if user == request.user:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                tags = []
                for tag_id in request.data.get('tags'):
                    tag = Tag.objects.get(pk=tag_id)
                    tags.append(tag)
                user.tags.set(tags)

                if request.data.get("followings") != None:
                    followings = []
                    for following_id in request.data.get('followings'):
                        following = User.objects.get(pk=following_id)
                        followings.append(following)
                    user.followings.set(followings)
                else:
                    pass
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"유저가 다릅니다."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        """회원 삭제(비활성화)"""
        user = get_object_or_404(User, pk=user_id)
        if user == request.user:
            user.is_active = False
            user.save()
            return Response({"message": "탈퇴 처리"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"유저가 다릅니다."}, status=status.HTTP_400_BAD_REQUEST)

class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "post 요청, 가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request):
        """로그아웃 기능입니다"""
        response = Response({"message": "로그아웃 완료"}, status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response

class TagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)