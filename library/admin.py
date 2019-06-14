from django.contrib import admin

from library.models import Author, Book, Form, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
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
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    exclude = ('vote_sum', 'vote_count')
    filter_horizontal = ('authors', 'genres', 'forms')
    list_display = ('name', 'get_authors', 'get_genres', 'get_forms', 'get_rating')
    list_filter = ('genres', 'forms', 'pub_date')
    ordering = ('-pub_date', )
    search_fields = ('name', 'authors__name')
