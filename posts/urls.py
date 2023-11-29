from django.urls import path

from posts.views import PostAPIView, PostDetailAPIView

urlpatterns = [
    path('', PostAPIView.as_view(), name="posts"),
    path('<int:pk>/', PostDetailAPIView.as_view()),
]