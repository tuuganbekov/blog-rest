import json
from rest_framework import views, response, status

from .models import Post
from .serializers import PostSerializer, PostModelSerializer


class PostAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    

class PostDetailAPIView(views.APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post)
            return response.Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Post.DoesNotExist:
            return response.Response(
                {"message": "Post does not exists"},
                status=status.HTTP_404_NOT_FOUND
            )

    
    def put(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostModelSerializer(post, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Post.DoesNotExist:
            return response.Response(
                {"message": "Post does not exists"},
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            post.delete()
            return response.Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except Post.DoesNotExist:
            return response.Response(
                {"message": "Post does not exists"},
                status=status.HTTP_404_NOT_FOUND
            )
