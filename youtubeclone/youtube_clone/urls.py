from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoList.as_view()),
    path('video/video_id/', views.VideoDetail.as_view())

]

    # path('video/', views.VideoList.as_view()),
    # path('video/<int:pk>/', views.VideoDetail.as_view())