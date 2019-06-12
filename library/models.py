from django.db import models


class Author(models.Model):
    name = models.CharField('имя', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    photo = models.ImageField('фото', upload_to='author/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Genre(models.Model):
    name = models.CharField('жанр', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Form(models.Model):
    name = models.CharField('форма', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'форма'
        verbose_name_plural = 'формы'


class Book(models.Model):
    name = models.CharField('название', max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField('описание', blank=True)

    pub_date = models.DateField('дата публикации', auto_now_add=True)

    authors = models.ManyToManyField(Author, verbose_name='авторы')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    forms = models.ManyToManyField(Form, verbose_name='формы')

    file = models.FileField('файл книги', upload_to='book/%Y/%m/%d/')
    thumbnail = models.ImageField('обложка', upload_to='thumbnail/%Y/%m/%d/', default='thumbnail/default-book.jpg')

    def __str__(self):
        return self.name

    def get_authors(self):
        return ', '.join([author.name for author in self.authors.all()])
    get_authors.short_description = 'авторы'

    def get_genres(self):
        return ', '.join([genre.name for genre in self.genres.all()])
    get_genres.short_description = 'жанры'

    def get_forms(self):
        return ', '.join([form.name for form in self.forms.all()])
    get_forms.short_description = 'формы'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
