from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from .models import Author, Book, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, BorrowRecordSerializer
from celery import current_app
from .tasks import generate_library_report
import os
from datetime import datetime
import json

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def create(self, request, *args, **kwargs):
        book_id = request.data.get("book")
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise ValidationError({"detail": "Book does not exist."})

        if book.available_copies <= 0:
            raise ValidationError({"detail": "No available copies for this book."})

        # Reduce the number of available copies
        book.available_copies -= 1
        book.save()

        return super().create(request, *args, **kwargs)

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


class ReportView(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='generate')
    def generate_report(self, request):

        generate_library_report.delay()
        return Response({"detail": "Report generation task initiated."}, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=['get'], url_path='latest')
    def latest_report(self, request):
        reports_path = os.path.join(os.getcwd(), "reports")
        latest_file = sorted(os.listdir(reports_path))[-1]
        with open(os.path.join(reports_path, latest_file), "r") as report_file:
            data = json.load(report_file)
        return Response(data, status=status.HTTP_200_OK)
