# TP1: Introduction to Django REST Framework - Core Components

## Objectives

- Install and set up Django REST Framework
- Create models for a RESTful API
- Implement serializers for data conversion
- Build API views using different approaches
- Configure URL routing
- Test the API using the browsable interface

## Prerequisites

- Basic knowledge of Django (models, views, URLs)
- Python environment setup
- Familiarity with HTTP methods (GET, POST, PUT, DELETE)

## 1. Installation and Setup

### 1.1 Create a New Django Project

If you haven't already created a Django project, do so now:

```bash
# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install Django
pip install django

# Create a new project
django-admin startproject library_api
cd library_api

# Create an app
python manage.py startapp books
```

### 1.2 Install Django REST Framework

```bash
pip install djangorestframework
```

### 1.3 Configure Settings

Update your `settings.py` file to include REST Framework:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Add Django REST Framework
    'books',  # Your app
]

# Add REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```

Don't forget to add your app to the `INSTALLED_APPS` list.

## 2. Creating Models for Your API

In this section, we'll create a simple library management system with books and authors.

Edit your `books/models.py` file:

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
```

Create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 3. Serializers Basics

Serializers allow complex data like querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML, or other content types.

Create a new file `books/serializers.py`:

```python
from rest_framework import serializers
from .models import Book, Author

# Simple ModelSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'date_of_birth']

# HyperlinkedModelSerializer with relationship
class BookSerializer(serializers.HyperlinkedModelSerializer):
    # Display author's name instead of id
    author_name = serializers.ReadOnlyField(source='author.name')
    
    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'author_name', 'publication_date', 
                  'isbn', 'pages', 'description']
```

The `ModelSerializer` provides a shortcut that automatically creates fields for all model attributes.

The `HyperlinkedModelSerializer` is similar but uses hyperlinks to represent relationships, rather than primary keys.

## 4. Views Architecture

Django REST Framework provides several classes to help you build API views:

### 4.1 Using APIView

First, let's implement views using the `APIView` class, which is similar to Django's `View`:

Add to `books/views.py`:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django.http import Http404

class BookList(APIView):
    """
    List all books, or create a new book.
    """
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    """
    Retrieve, update or delete a book instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### 4.2 Using ViewSets

ViewSets allow you to combine the logic for a set of related views in a single class:

Add to `books/views.py`:

```python
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Alternative to the BookList and BookDetail classes
class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

## 5. URL Routing with DefaultRouter

The DefaultRouter class automatically creates the URL patterns for your ViewSets:

Create `books/urls.py`:

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
```

Now, update your project's main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

## 6. Building Your First Complete RESTful API

We've now set up a complete RESTful API that supports:

- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book
- `GET /api/books/{id}/` - Retrieve a specific book
- `PUT /api/books/{id}/` - Update a specific book
- `DELETE /api/books/{id}/` - Delete a specific book

And similar endpoints for authors.

Let's add some sample data:

```python
# books/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from books.models import Author, Book
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        Author.objects.all().delete()
        Book.objects.all().delete()
        
        # Create authors
        author1 = Author.objects.create(
            name='J.K. Rowling',
            bio='British author best known for the Harry Potter series',
            date_of_birth=date(1965, 7, 31)
        )
        
        author2 = Author.objects.create(
            name='George Orwell',
            bio='English novelist, essayist, and critic',
            date_of_birth=date(1903, 6, 25)
        )
        
        # Create books
        Book.objects.create(
            title='Harry Potter and the Philosopher\'s Stone',
            author=author1,
            publication_date=date(1997, 6, 26),
            isbn='9780747532743',
            pages=223,
            description='The first book in the Harry Potter series'
        )
        
        Book.objects.create(
            title='1984',
            author=author2,
            publication_date=date(1949, 6, 8),
            isbn='9780451524935',
            pages=328,
            description='A dystopian social science fiction novel'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
```

Make sure to create the directory structure for this command:

```bash
mkdir -p books/management/commands
touch books/management/commands/__init__.py
touch books/management/__init__.py
```

Run the command to populate the database:

```bash
python manage.py populate_db
```

## 7. Testing Endpoints with the Browsable API

Django REST Framework comes with a powerful browsable API that you can use to interact with your endpoints.

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Open your browser and go to:
   - <http://127.0.0.1:8000/api/books/>
   - <http://127.0.0.1:8000/api/authors/>

3. The browsable API allows you to:
   - View all records
   - View individual records
   - Create new records through forms
   - Edit and delete existing records
   - Authenticate with user credentials

### Using cURL to Test Your API

You can also test your API using command-line tools like cURL:

```bash
# Get all books
curl -X GET http://127.0.0.1:8000/api/books/

# Get a specific book
curl -X GET http://127.0.0.1:8000/api/books/1/

# Create a new book (requires authentication)
curl -X POST -H "Content-Type: application/json" -d '{"title":"New Book","author":1,"publication_date":"2023-01-01","isbn":"1234567890123","pages":200,"description":"A new book"}' http://127.0.0.1:8000/api/books/

# Update a book
curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Book Title","author":1,"publication_date":"2023-01-01","isbn":"1234567890123","pages":200,"description":"Updated description"}' http://127.0.0.1:8000/api/books/1/

# Delete a book
curl -X DELETE http://127.0.0.1:8000/api/books/1/
```

## Conclusion

In this tutorial, you've learned:

- How to set up Django REST Framework
- Creating models for your API
- Implementing serializers to convert between Python objects and JSON
- Building views using both APIView and ViewSets
- Configuring URL routing with DefaultRouter
- Testing your API endpoints

## Exercises

1. Add a new model `Review` with a relationship to `Book` and implement the API endpoints for it.
2. Implement filtering on the Book API to allow searching by title or author name.
3. Add pagination to your API to limit the number of results per page.
4. Implement custom validation for the ISBN field to ensure it's a valid ISBN format.
5. Add authentication requirements so that only authenticated users can create, update, or delete records.

## Resources for Further Learning

- [Django REST Framework Official Documentation](https://www.django-rest-framework.org/)
- [Django REST Framework Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)
- [Classy Django REST Framework](https://www.cdrf.co/) - A reference for DRF class-based views
