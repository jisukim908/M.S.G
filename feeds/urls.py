from django.urls import path
from feeds import views

urlpatterns = [
    path('/api/channel/{user_id}/', views.ChannelsView(), name="channel_view"),
    path('/api/channel/admin/', views.ChannelAdminView(), name="channel_admin_view"),
    path('/api/channel/admin/{feed_id}/', views.ChannelAdminView(), name="update_view"),
]