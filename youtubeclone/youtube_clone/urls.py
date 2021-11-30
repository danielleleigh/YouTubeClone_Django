from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('comment/<slug:video_id>/', views.CommentDetail.as_view()),

    path('reply/', views.ReplyList.as_view()),
    path('reply/<slug:video_id>/', views.ReplyDetail.as_view())


]

    # path('video/', views.VideoList.as_view()),
    # path('video/<int:pk>/', views.VideoDetail.as_view())