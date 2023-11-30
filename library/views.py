from rest_framework.decorators import api_view
from rest_framework import response, status

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


@api_view(["GET"])
def author_list(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "GET":
        serializer = BookSerializer(book)
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    elif request.method == "PATCH":
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    elif request.method == "DELETE":
        book.delete()
        return response.Response(
            status=status.HTTP_204_NO_CONTENT
        )
