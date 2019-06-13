from django.shortcuts import render, get_object_or_404

from library.models import Author, Book


def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


def authors(request):
    author_list = Author.objects.all()
    return render(request, 'library/authors.html', {'authors': author_list})


def genres(request):
    books = Book.objects.all()
    return render(request, 'library/genres.html', {'books': books})


def forms(request):
    books = Book.objects.all()
    return render(request, 'library/forms.html', {'books': books})
