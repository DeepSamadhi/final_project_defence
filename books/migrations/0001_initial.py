# Generated by Django 4.1.3 on 2022-11-30 12:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('image', models.URLField()),
                ('genre', models.CharField(choices=[('Fiction', 'Fiction'), ('Fantasy', 'Fantasy'), ('Novel', 'Novel'), ('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Crime', 'Crime'), ('Horror', 'Horror'), ('Memoir', 'Memoir'), ('Biography', 'Biography'), ('Poetry', 'Poetry'), ('History', 'History'), ('Novel', 'Novel'), ('Novel', 'Novel'), ('Other', 'Other')], max_length=30)),
                ('year_of_publication', models.PositiveIntegerField()),
                ('borrower', models.CharField(max_length=50, null=True)),
                ('borrow_counter', models.PositiveBigIntegerField(blank=True, null=True)),
                ('return_date', models.DurationField(null=True)),
                ('is_borrow', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='books.autors')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='books.publishers')),
            ],
        ),
    ]
