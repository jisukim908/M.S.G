from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from users import views

urlpatterns = [
    # 로그인
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 토큰 재발행
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 회원가입
    path('signup/', views.UserSignupView.as_view(), name="user_view"),
    # 로그아웃
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    # 태그 api
    path('tag/', views.TagView.as_view(), name='tag_view'),
    # 유저 프로필 api
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name="user_profile"),
    # 팔로우
    path('follow/<int:user_id>/', views.FollowView.as_view(), name='follow_view')
]
