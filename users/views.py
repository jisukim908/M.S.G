from rest_framework.views import APIView
from rest_framework.response import Response



class FollowView(APIView):
    def post(self, request, user_id):
        #follow기능을 담당
        pass

class UserProfileView(APIView):
    def get(self, request):
        """서용자 정보를 response 합니다"""
        return Response({"message": "get 요청입니다!"})
    
    def put(self, request):
        """회원 정보를 수정합니다"""
        return Response({"message": "put 요청입니다!"})

    def delete(self, request):
        """회원 삭제(비활성화)"""
        return Response({"message": "delete 요청입니다!"})


class UserSignupView(APIView):
    def post(self, request):
        """서용자 정보를 입력받아 회원가입을 진행합니다"""
        return Response({"message": "post 요청입니다!"})

class UserLoginView(APIView):
    def post(self, reqeuest):
        """로그인 기능입니다"""
        return Response({"message": "login 요청입니다"})


class UserLogoutView(APIView):
    def post(self, reqeuest):
        """로그아웃 기능입니다"""
        return Response({"message": "logout 요청입니다"})
