from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ChannelsView(APIView):
    def get(self, request, user_id):
        # 개인 채널의 간단 정보, 개인의 전체 동영상 보기, 
        # 로그인 없이 볼 수 있음
        return Response({"message": "channel get 요청입니다!"})

class ChannelAdminView(APIView):
    def get(self, request):
        #개인 채널 관리 뷰
        return Response({"message": "채널 get 요청입니다!"})

    def post(self, request, feed_id):
        # 관리페이지 안에서 수정
        return Response({"message": "channel post 요청입니다!"})

    def delete(self, request, feed_id):
        # 관리페이지 안에서 삭제
        return Response({"message": "channel delete 요청입니다!"})
