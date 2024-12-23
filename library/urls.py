from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BorrowRecordViewSet, ReportView

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='author')
router.register('books', BookViewSet, basename='book')
router.register('borrow', BorrowRecordViewSet, basename='borrow')
router.register('reports', ReportView, basename='report')

urlpatterns = [
    path('', include(router.urls)),
]