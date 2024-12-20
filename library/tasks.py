from celery import shared_task
from .models import Author, Book, BorrowRecord
import os
import json
from datetime import datetime

@shared_task
def generate_library_report():
    total_authors = Author.objects.count()
    total_books = Book.objects.count()
    total_borrowed = BorrowRecord.objects.filter(return_date__isnull=True).count()

    report = {
        "total_authors": total_authors,
        "total_books": total_books,
        "total_borrowed": total_borrowed,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(report_path, "w") as report_file:
        json.dump(report, report_file)