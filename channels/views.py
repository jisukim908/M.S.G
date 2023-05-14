from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import render, redirect
from feeds.models import Feed
from users.models import User
from feeds.serializers import FeedDetailSerializer, FeedCreateSerializer
from channels.serializers import ChannelViewSerializer
from hitcount.views import HitCountDetailView

# 채널 정보
class ChannelinfoView(APIView):
    def get(self, request, user_id):
        info = get_object_or_404(User, pk=user_id)
        serializer = ChannelViewSerializer(info)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 채널의 영상 또는 게시글 보기
class ChannelsView(APIView):
    def get(self, request, user_id):
        # 개인 채널의 간단 정보, 개인의 전체 동영상 보기, 
        # 로그인 없이 볼 수 있음, 로그인되어있을 시, 구독 표시 있기 => 이건 프론트에서 구현해야할 듯
        feeds = Feed.objects.filter(user_id=user_id)
        serializer = FeedDetailSerializer(feeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ChannelAdminView(APIView, HitCountDetailView):
    model = Feed   

    # 채널 피드 자세히 보기
    def get(self, request, user_id, feed_id):
        #개인 채널 관리 뷰
        #업로드한 동영상 또는 게시글 확인할 수 있음
        permission_classes = [permissions.IsAuthenticated]
        feeds = Feed.objects.filter(id = feed_id)
        serializer = FeedDetailSerializer(feeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # 관리페이지 안에서 수정
    def put(self, request, user_id, feed_id):
        permission_classes = [permissions.IsAuthenticated]
        # if request.user.id == user_id:
        feed = get_object_or_404(Feed, id=feed_id)
        serializer = FeedCreateSerializer(feed, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #    return Response("권한이 없습니다.")

    # 관리페이지 안에서 삭제
    def delete(self, request, user_id, feed_id):
        # if request.user.id == user_id:
        permission_classes = [permissions.IsAuthenticated]
        feed = get_object_or_404(Feed, id=feed_id)
        feed.delete()
        return Response("삭제되었습니다.",status=status.HTTP_204_NO_CONTENT)
        #else:
        #    return Response("권한이 없습니다.")