from django.urls import path
from channels import views

urlpatterns = [
    path('/api/channel/{user_id}/', views.ChannelsView().as_view(), name="channel_view"),
    path('/api/channel/admin/', views.ChannelAdminView().as_view(), name="channel_admin_view"),
    path('/api/channel/admin/{feed_id}/', views.ChannelAdminView().as_view(), name="update_view"),
]