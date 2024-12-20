from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Book, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, BorrowRecordSerializer
from datetime import datetime

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    @action(detail=True, methods=['put'], url_path='return')
    def return_book(self, request, pk=None):
        borrow_record = self.get_object()
        if borrow_record.return_date is not None:
            return Response({"detail": "Book already returned."}, status=status.HTTP_400_BAD_REQUEST)

        borrow_record.return_date = datetime.now().date()
        borrow_record.book.available_copies += 1
        borrow_record.book.save()
        borrow_record.save()
        return Response({"detail": "Book returned successfully."}, status=status.HTTP_200_OK)