# Generated by Django 4.1.3 on 2022-12-05 08:42

import books.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='images/', validators=[books.validators.image_size_validator]),
        ),
    ]
