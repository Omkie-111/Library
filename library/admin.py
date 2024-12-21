from django.contrib import admin
from .models import Author, Book, BorrowRecord

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies')
    search_fields = ('title', 'isbn')
    list_filter = ('author',)


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrowed_by', 'borrow_date', 'return_date')
    search_fields = ('borrowed_by', 'book__title')
    list_filter = ('borrow_date', 'return_date')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
