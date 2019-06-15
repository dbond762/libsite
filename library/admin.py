from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from library.models import Author, Book, Form, Genre


@admin.register(Author)
class AuthorAdmin(AdminImageMixin, admin.ModelAdmin):
    ordering = ('name', )
    search_fields = ('name', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ('name', )
    search_fields = ('name', )


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    ordering = ('name', )
    search_fields = ('name', )


@admin.register(Book)
class BookAdmin(AdminImageMixin, admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    exclude = ('vote_sum', 'vote_count', 'rating')
    filter_horizontal = ('authors', 'genres', 'forms')
    list_display = ('name', 'get_authors', 'get_genres', 'get_forms', 'rating')
    list_filter = ('genres', 'forms', 'pub_date')
    ordering = ('-rating', )
    search_fields = ('name', 'authors__name')
