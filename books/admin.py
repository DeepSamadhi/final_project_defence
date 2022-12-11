from django.contrib import admin

# Register your models here.

from .models import Books, Autors, Publishers


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
   list_display = ('title', 'autor', 'publisher', 'genre', 'owner', 'image', 'is_borrow', 'return_date', 'year_of_publication')
   list_filter = ('genre', )
   fieldsets = (
        (None, {
            'fields': ('title', 'autor', 'publisher', 'genre', 'owner', 'image', 'is_borrow', 'return_date', 'year_of_publication')
        }),
    )   

@admin.register(Autors)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )


@admin.register(Publishers)
class BooksAdmin(admin.ModelAdmin):
    search_fields = ("publisher_name__startswith", )