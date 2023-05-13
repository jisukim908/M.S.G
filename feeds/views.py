from rest_framework.views import APIView
from feeds.models import Feed, Comment
from feeds.serializers import (
    FeedListSerializer,
    FeedCreateSerializer,
    FeedDetailSerializer,
    CommentSerializer,
    FeedSearchSerializer
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from hitcount.views import HitCountDetailView
from django.views.generic import ListView
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated


class FeedListView(APIView, ListView):
    model = Feed
    paginate_by = 12

    def get(self, request):
        ### -created_at 이 아니라 created_date 로 수정해주어야 함!!
        feeds = Feed.objects.all().order_by("-created_date")
        seriailizer = FeedListSerializer(feeds, many=True)
        return Response(seriailizer.data, status=status.HTTP_200_OK)


class FeedCommentsView(APIView):
    def get(self, request, feed_id):
        # 해당 게시글 댓글 가져옴
        comments = Comment.objects.filter(feed__id=feed_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, feed_id):
        # 댓글 가져오기
        comments = Comment.objects.filter(feed__id=feed_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, feed_id):
        # 댓글 생성
        feeds = get_object_or_404(Feed, pk=feed_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, feed=feeds)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, comment_id):
        # 댓글 수정
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "댓글이 없습니다."}, status=404)

        if comment.user != request.user:
            return Response({"error": "댓글 작성자만 수정할 수 있습니다."}, status=403)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, comment_id):
        # 댓글 삭제
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "댓글이 없습니다."}, status=404)

        if comment.user != request.user:
            return Response({"error": "댓글 작성자만 삭제할 수 있습니다."}, status=403)

        comment.delete()
        return Response({"message": "삭제되었습니다."}, status=204)


class CommentsLikeView(APIView):
    permission_classes = [IsAuthenticated]

    # 좋아요
    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "댓글이 없습니다."}, status=404)

        comment.like_count += 1
        comment.save()
        return Response(status=204)


class CommentsDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    # 싫어요
    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "댓글이 없습니다."}, status=404)

        comment.dislike_count += 1
        comment.save()
        return Response(status=204)


class FeedSearchView(generics.ListCreateAPIView):
    search_fields = ["title", "context", "tag__name"]
    filter_backends = (filters.SearchFilter,)
    queryset = Feed.objects.all()
    serializer_class = FeedSearchSerializer
    
    
class FeedDetailView(APIView, HitCountDetailView):
    #feed 상세페이지

    # 조회수
    model = Feed    
    
    ### authonr_id 추가해주어야함!!
    def get(self, request, author_id, feed_id):
        feed = get_object_or_404(Feed, id=feed_id)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # feed 조회수 기능
    def post(self, request, author_id, feed_id):
        feed = get_object_or_404(Feed, id=feed_id)
        feed.click
        return Response("조회수 +1", status=status.HTTP_200_OK)


class FeedCreateView(APIView):
    # feed 만들기 기능. 
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FeedCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FeedLikeView(APIView):
    # feed 좋아요 기능 
    permission_classes = [IsAuthenticated]

    def post(self, request, feed_id):
        feed = get_object_or_404(Feed, id=feed_id)
        if request.user in feed.likes.all():
            feed.likes.remove(request.user) # like 요청 유저가 없으면 제거
            return Response("좋아요", status=status.HTTP_200_OK)
        else:
            feed.likes.add(request.user) #like 요청 유저가 없으면 추가
            return Response("좋아요 취소!", status=status.HTTP_200_OK)
