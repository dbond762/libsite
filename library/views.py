from django.shortcuts import render

from library.models import Book


def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})


def authors(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})


def genres(request):
    books = Book.objects.all()
    return render(request, 'library/genres.html', {'books': books})


def forms(request):
    books = Book.objects.all()
    return render(request, 'library/forms.html', {'books': books})
