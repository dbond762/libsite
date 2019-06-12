# Generated by Django 2.2.2 on 2019-06-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to='author/%Y/%m/%d/', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='форма')),
            ],
            options={
                'verbose_name': 'форма',
                'verbose_name_plural': 'формы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='жанр')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='дата публикации')),
                ('file', models.FileField(upload_to='book/%Y/%m/%d/', verbose_name='файл книги')),
                ('thumbnail', models.ImageField(upload_to='thumbnail/%Y/%m/%d/', verbose_name='обложка')),
                ('authors', models.ManyToManyField(to='library.Author', verbose_name='авторы')),
                ('forms', models.ManyToManyField(to='library.Form', verbose_name='формы')),
                ('genres', models.ManyToManyField(to='library.Genre', verbose_name='жанры')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
