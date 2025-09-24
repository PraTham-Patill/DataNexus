from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    List all books or create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a book instance
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
