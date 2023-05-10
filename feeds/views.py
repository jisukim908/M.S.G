from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class FeedListView():
    def get(self, request):
        #전체 피드 최신순으로 보기 
        #순위 등 포함
        return Response({"message": "feedlist get 요청입니다!"})

class CommentsView():
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

class FeedDetailView():
    def get(self, request, post_id):
        #게시글 상세, 게시글 작성자 정보
        return Response({"message": "get 요청입니다!"})


class FeedCreateView():
    def post(self, request):
        #게시글 쓰기
        return Response({"message": "feed post 요청입니다!"})

    def update(self, request, post_id):
        #게시글 수정
        return Response({"message": "feed update 요청입니다!"})

    def delete(self, request, post_id):
        #게시글 삭제
        return Response({"message": "feed delete 요청입니다!"})


