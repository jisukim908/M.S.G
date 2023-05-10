from rest_framework.views import APIView
from .models import Feed, Comment
from .serializers import FeedSerializer, CommentSerializer, FeedListSerializer
from rest_framework.response import Response
from hitcount.views import HitCountDetailView
from rest_framework import generics, filters


class FeedListView(APIView):
    def get(self, request):
        feeds = Feed.objects.all().order_by("-created_at")
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)


class FeedDetailView(APIView, HitCountDetailView):
    # 조회수
    model = Feed
    count_hit = True

    # 탬플릿에서 조회수 나타내기
    # {# the total hits for the object #}
    # {{ hitcount.total_hits }}

    def get(self, request, post_id):
        try:
            feed = Feed.objects.get(id=post_id)
        except Feed.DoesNotExist:
            return Response({"error": "피드가 없습니다."}, status=404)

        serializer = FeedSerializer(feed)
        return Response(serializer.data)


class FeedCreateView(APIView):
    def post(self, request):
        # 게시글 작성
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class CommentsView(APIView):
    def get(self, request):
        # 댓글 가져오기
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 댓글 생성
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, comment_id):
        # 댓글 수정
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "댓글이 없습니다."}, status=404)

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
        comment.delete()
        return Response({"message": "삭제되었습니다."}, status=204)


class CommentsLikeView(APIView):
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
    # 싫어요 ㅠ
    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"error": "댓글이 없습니다."}, status=404)

        comment.dislike_count += 1
        comment.save()

        return Response(status=204)


class FeedSearchView(generics.ListCreateAPIView):
    search_fields = ["title", "context"]
    filter_backends = (filters.SearchFilter,)
    queryset = Feed.objects.all()
    serializer_class = FeedListSerializer
