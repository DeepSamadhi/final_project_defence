# Generated by Django 4.1.3 on 2022-12-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_books_return_date_alter_books_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]
