# Generated by Django 2.2.2 on 2019-06-14 17:08

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20190613_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(default='author/default-photo.jpg', upload_to='author/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=sorl.thumbnail.fields.ImageField(default='thumbnail/default-book.jpg', upload_to='thumbnail/%Y/%m/%d/', verbose_name='обложка'),
        ),
    ]
