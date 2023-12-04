from django.urls import path

from posts.views import (
    PostAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostDetailView,
    PostUpdateAPIView,
    PostDeleteAPIView
    )

urlpatterns = [
    path('', PostAPIView.as_view(), name="posts"),
    path('<int:pk>/', PostDetailView.as_view()),
    path('generics/', PostListAPIView.as_view()),
    path('generics/<int:pk>/', PostDetailAPIView.as_view()),
    path('generics/update/<int:pk>/', PostUpdateAPIView.as_view()),
    path('generics/delete/<int:pk>/', PostDeleteAPIView.as_view()),
]