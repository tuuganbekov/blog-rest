from django.urls import path

from .views import author_list, book_list, book_detail


urlpatterns = [
    path('authors/', author_list),
    path('books/', book_list),
    path('books/<int:pk>/', book_detail),
]