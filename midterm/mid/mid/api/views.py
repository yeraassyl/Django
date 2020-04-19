from mid.api.models import Book,Journal
from mid.api.serializers import BookSerializer,JournalSerializer
from rest_framework import viewsets

class BookListViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class JournalListViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer