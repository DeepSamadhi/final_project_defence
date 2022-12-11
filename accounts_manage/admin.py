from django.contrib import admin

from .models import LibraryUser, UserProfile

@admin.register(LibraryUser)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['username', 'date_joined', 'is_staff', 'is_superuser']


@admin.register(UserProfile)
class BooksAdmin(admin.ModelAdmin):
   list_display = ['first_name', 'last_name', 'age', 'user']