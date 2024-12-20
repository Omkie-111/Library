from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book


class AuthorViewSetTests(APITestCase):
    def setUp(self):
        self.author_data = {
            'name': 'Test Author',
            'bio': 'This is a test author bio.',
        }
        self.author = Author.objects.create(**self.author_data)

    def test_author_list(self):
        """Test listing all authors"""
        url = '/authors/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.author.name)

    def test_author_create(self):
        """Test creating a new author"""
        url = '/authors/'
        data = {
            'name': 'New Author',
            'bio': 'This is a new author bio.',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)
        self.assertEqual(Author.objects.get(id=response.data['id']).name, 'New Author')

    def test_author_update(self):
        """Test updating an existing author"""
        url = f'/authors/{self.author.id}/'
        data = {
            'name': 'Updated Author',
            'bio': 'Updated bio.',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'Updated Author')

    def test_author_delete(self):
        """Test deleting an author"""
        url = f'/authors/{self.author.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 0)


class BookViewSetTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author', bio='Bio')
        self.book_data = {
            'title': 'Test Book',
            'author': self.author,  
            'isbn': '1234567890123',
            'available_copies': 5,
        }
        self.book = Book.objects.create(**self.book_data)

    def test_book_list(self):
        """Test listing all books"""
        url = '/books/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_book_create(self):
        """Test creating a new book"""
        url = '/books/'
        data = {
            'title': 'New Book',
            'author': self.author.id,  
            'isbn': '9876543210987',
            'available_copies': 10,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_book_update(self):
        """Test updating an existing book"""
        url = f'/books/{self.book.id}/'
        data = {
            'title': 'Updated Book',
            'author': self.author.id,  
            'isbn': '1122334455667',
            'available_copies': 7,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_book_delete(self):
        """Test deleting a book"""
        url = f'/books/{self.book.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
