import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")  # replace myproject with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


if __name__ == "__main__":
    # Example usage
    print("Books by Author John Doe:")
    for book in get_books_by_author("John Doe"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in get_books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian of Central Library:")
    print(get_librarian_for_library("Central Library"))
