from django.urls import path
from feeds import views

urlpatterns = [
    path('api/feeds/', views.FeedListView.as_view(), name="feedlist"),
    path('api/feeds/<int:feed_id>/', views.FeedDetailView.as_view(), name="feed_detail"),
    path('api/feeds/<int:feed_id>/likes/', views.LikeView.as_view(), name="likes_feed"),
]