from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from library.models import Author, Book, Form, Genre


def home(request):
    books = Book.objects.order_by('-rating', '-pub_date')
    return render(request, 'library/home.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


def vote(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    url = request.POST.get('url', reverse('library:home'))

    try:
        rating = int(request.POST['rating'])
        if rating < 1 or rating > 5:
            raise IndexError
    except (KeyError, TypeError, IndexError):
        return HttpResponseRedirect(url)

    book.vote(rating)
    book.save()
    return HttpResponseRedirect(url)


def authors(request):
    author_list = Author.objects.all()
    return render(request, 'library/authors.html', {'authors': author_list})


def author_books(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(authors__pk=pk)
    return render(request, 'library/author_books.html', {'author': author, 'books': books})


def genres(request):
    genre_list = Genre.objects.all()

    try:
        active_genre = int(request.GET['active-genre'])
        books = Book.objects.filter(genres__id=active_genre)
    except (KeyError, TypeError):
        books = Book.objects.all()

    return render(request, 'library/genres.html', {'genres': genre_list, 'books': books})


def forms(request):
    form_list = Form.objects.all()

    try:
        active_form = int(request.GET['active-form'])
        books = Book.objects.filter(forms__id=active_form)
    except (KeyError, TypeError):
        books = Book.objects.all()

    return render(request, 'library/forms.html', {'forms': form_list, 'books': books})
