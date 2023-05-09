from rest_framework.views import APIView
from feeds.models import Feed
from feeds.serializers import FeedListSerializer, FeedCreateSerializer, FeedDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from hitcount.views import HitCountDetailView


class FeedListView(APIView):
    ### 게시글마다 각각의 조회수가 필요할 것 같아요
    model = Feed    
    count_hit = True 

    def get(self, request):
        feeds = Feed.objects.all().order_by("-created_at")
        seriailizer = FeedListSerializer(feeds, many=True)
        return Response(seriailizer.data, status=status.HTTP_200_OK)

class CommentsView(APIView):
    def get(self, request):
        #댓글 가져오기
        return Response({"message": "comment get 요청입니다!"})

    def post(self, request):
        #댓글 생성
        return Response({"message": "comment post 요청입니다!"})

    def update(self, request, comment_id):
        #댓글 수정
        return Response({"message": "comment update 요청입니다!"})

    def delete(self, request, comment_id):
        #댓글 삭제
        return Response({"message": "comment delete 요청입니다!"})

class FeedDetailView(APIView, HitCountDetailView):
    # 조회수
    model = Feed    
    count_hit = True 

    # 탬플릿에서 조회수 나타내기
    # {# the total hits for the object #}
    # {{ hitcount.total_hits }}

    def get(self, request, feed_id):
        feed = get_object_or_404(Feed, id=feed_id)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FeedCreateView(APIView):
    def post(self, request):
        serializer = FeedCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, feed_id):
        feed = get_object_or_404(Feed, id=feed_id)
        if request.user == feed.user:
            serializer = FeedCreateSerializer(feed, data=serializer.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("수정 권한이 없습니다", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, feed_id):
        feed = get_object_or_404(Feed, id=feed_id)
        if request.user == feed.user:
            feed.delete()
            return Response("게시글이 삭제되었습니다", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("삭제 권한이 없습니다", status=status.HTTP_403_FORBIDDEN)
