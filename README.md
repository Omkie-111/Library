# Library Management API

This is a simple API built using Django and Django Rest Framework for managing books and authors in a library system.

## Features

- CRUD operations for authors and books.
- Borrow functionality for users to borrow books.
- Generate reports on book availability and borrowed books.
- Use of Django Rest Framework's `APITestCase` for testing API endpoints.

## Table of Contents

1. [**Installation**](#installation)
2. [**Running the Project**](#running-the-project)
3. [**Docker Setup**](#docker-setup)
4. [**API Endpoints**](#api-endpoints)
    - [**Authors Endpoints**](#authors)
    - [**Books Endpoints**](#books)
    - [**Borrow Endpoints**](#borrow)
    - [**Reports Endpoints**](#reports)
5. [**Testing**](#testing)
6. [**Deployment**](#deployment)

---

## Installation

### 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/library-management-api.git
cd library-management-api
```

### 2. Set up Virtual Environment

It's a good practice to create a virtual environment for the project. To create one and activate it, run the following:

```bash
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
```

### 3. Install Dependencies

Once your virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Make sure that your database is set up. You can use the default SQLite database or configure PostgreSQL/MySQL as per your project requirements. 

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 5. Create a Superuser

If you want to access the admin panel, you can create a superuser using the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin credentials.

---

## Running the Project

To run the development server, execute:

```bash
python manage.py runserver
```

This will start the server on `http://127.0.0.1:8000/` by default. For further live testing check the deployment section.

---

## Docker Setup

To set up the project with Docker, follow these steps:

1. **Build the Docker Image**

   ```bash
   docker-compose build
   ```

2. **Run the Docker Container**

   ```bash
   docker-compose up
   ```

   This will start the containers, including Django, PostgreSQL, and any other necessary services, and make the project accessible on `http://127.0.0.1:8000/`.

---

## API Endpoints Description

### 1. Authors

#### - `GET /authors/`
- **Description**: Retrieves a list of all authors in the system.
- **Request**: `GET` request to the `/authors/` endpoint.
- **Response**: Returns a list of authors with their details, such as name, bio, and ID.

**Example Response**:
```json
[
  {
    "id": 1,
    "name": "Author Name",
    "bio": "Biography of the author"
  },
  {
    "id": 2,
    "name": "Another Author",
    "bio": "Biography of another author"
  }
]
```

#### - `POST /authors/`
- **Description**: Creates a new author in the system.
- **Request**: `POST` request to the `/authors/` endpoint with a JSON payload containing the author's `name` and `bio`.
- **Response**: Returns the created author with an assigned `id`.

**Example Request**:
```json
{
  "name": "New Author",
  "bio": "Biography of the new author"
}
```

**Example Response**:
```json
{
  "id": 3,
  "name": "New Author",
  "bio": "Biography of the new author"
}
```

#### - `GET /authors/<id>/`
- **Description**: Retrieves a specific author based on their ID.
- **Request**: `GET` request to `/authors/<id>/` where `<id>` is the author's ID.
- **Response**: Returns the details of the specified author.

**Example Response**:
```json
{
  "id": 1,
  "name": "Author Name",
  "bio": "Biography of the author"
}
```

#### - `PUT /authors/<id>/`
- **Description**: Updates the details of a specific author based on their ID.
- **Request**: `PUT` request to `/authors/<id>/` with a JSON payload containing updated author details.
- **Response**: Returns the updated author details.

**Example Request**:
```json
{
  "name": "Updated Author",
  "bio": "Updated biography of the author"
}
```

**Example Response**:
```json
{
  "id": 1,
  "name": "Updated Author",
  "bio": "Updated biography of the author"
}
```

#### - `DELETE /authors/<id>/`
- **Description**: Deletes a specific author based on their ID.
- **Request**: `DELETE` request to `/authors/<id>/`.
- **Response**: Returns a message confirming the author was deleted.

**Example Response**:
```json
{
  "detail": "Deleted"
}
```

### 2. Books

#### - `GET /books/`
- **Description**: Retrieves a list of all books in the system.
- **Request**: `GET` request to the `/books/` endpoint.
- **Response**: Returns a list of books with their details such as title, author, ISBN, available copies, and book ID.

**Example Response**:
```json
[
  {
    "id": 1,
    "title": "Book Title",
    "author": 1,
    "isbn": "9781234567890",
    "available_copies": 5
  }
]
```

#### - `POST /books/`
- **Description**: Adds a new book to the system.
- **Request**: `POST` request to `/books/` with a JSON payload containing the book's `title`, `author`, `isbn`, and `available_copies`.
- **Response**: Returns the created book with its `id` and other details.

**Example Request**:
```json
{
  "title": "New Book",
  "author": 1,
  "isbn": "9789876543210",
  "available_copies": 10
}
```

**Example Response**:
```json
{
  "id": 2,
  "title": "New Book",
  "author": 1,
  "isbn": "9789876543210",
  "available_copies": 10
}
```

#### - `GET /books/<id>/`
- **Description**: Retrieves a specific book based on its ID.
- **Request**: `GET` request to `/books/<id>/` where `<id>` is the book's ID.
- **Response**: Returns the details of the specified book.

**Example Response**:
```json
{
  "id": 1,
  "title": "Book Title",
  "author": 1,
  "isbn": "9781234567890",
  "available_copies": 5
}
```

#### - `PUT /books/<id>/`
- **Description**: Updates the details of a specific book based on its ID.
- **Request**: `PUT` request to `/books/<id>/` with a JSON payload containing updated book details.
- **Response**: Returns the updated book details.

**Example Request**:
```json
{
  "title": "Updated Book Title",
  "author": 1,
  "isbn": "9781234567890",
  "available_copies": 6
}
```

**Example Response**:
```json
{
  "id": 1,
  "title": "Updated Book Title",
  "author": 1,
  "isbn": "9781234567890",
  "available_copies": 6
}
```

#### - `DELETE /books/<id>/`
- **Description**: Deletes a specific book based on its ID.
- **Request**: `DELETE` request to `/books/<id>/`.
- **Response**: Returns a message confirming the book was deleted.

**Example Response**:
```json
{
  "detail": "Deleted"
}
```

### 3. Borrow Records

#### - `POST /borrow/`
- **Description**: Creates a new borrow record, marking a book as borrowed and reducing its available copies by 1.
- **Request**: `POST` request to `/borrow/` with a JSON payload containing `borrowed_by` and `book`.
- **Response**: Returns the created borrow record.

**Example Request**:
```json
{
  "borrowed_by": "",
  "book": Book1
}
```

**Example Response**:
```json
{
  "id": 1,
  "book": 1,
  "user": 2,
  "borrow_date": "2024-12-20",
  "return_date": null
}
```

#### - `PUT /borrow/<id>/return/`
- **Description**: Marks a borrowed book as returned and updates the available copies by increasing it by 1.
- **Request**: `PUT` request to `/borrow/<id>/return/` where `<id>` is the borrow record's ID.
- **Response**: Returns the updated borrow record with `return_date` set and the book's `available_copies` incremented.

**Example Request**:
```bash
PUT http://127.0.0.1:8000/borrow/1/return/
```

**Example Response**:
```json
{
  "id": 1,
  "book": 1,
  "user": 2,
  "borrow_date": "2024-12-20",
  "return_date": "2025-01-20"
}
```

### 4. Reports

#### - `GET /reports/latest/`
- **Description**: Retrieves the latest report generated by the background task, showing data such as book availability, borrowed book stats, etc.
- **Request**: `GET` request to `/reports/latest/`.
- **Response**: Returns the latest generated report.

**Example Response**:
```json
{
  "report_id": 1,
  "books_report": {
    "available_books": 50,
    "borrowed_books": 20
  }
}
```

#### - `POST /reports/generate/`
- **Description**: Triggers the generation of a new report in the background using a Celery task. This endpoint generates the latest report asynchronously.
- **Request**: `POST` request to `/reports/generate/`.
- **Response**: A message indicating that the report generation is in progress.

**Example Request**:
```bash
POST http://127.0.0.1:8000/reports/generate/
```

**Example Response**:
```json
{
  "detail": "Report generation task initiated."
}
```

---

## Testing

To run the tests, execute the following command:

```bash
python manage.py test
```

This will run the test cases and provide feedback on the API functionality, ensuring that all CRUD operations for authors, books, borrowing, and report generation are working correctly.

---

## Deployment

This project is deployed on Koyeb and is live at [Live Site](https://fixed-pattie-omkie-fe37b6cc.koyeb.app/)

---
