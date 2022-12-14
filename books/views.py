from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime, timedelta

import cloudinary


from books.models import Books, Autors, Publishers
from accounts_manage.models import LibraryUser
from books.forms import CreateBookForm, UpdateBookForm              # CreateAutorForm




UserModel = get_user_model()



def book_create(request):    # TODO: check how to create with CBV and use class methods for get data and DB search
    if request.method == 'GET':
        form = CreateBookForm()
        context = {
            'form': form
        }
        return render(request,'book-create.html', context)
    else:
        try:
            autor_exist = Autors.objects.get(name=request.POST['autor'])
            autor = autor_exist
        except:
            autor = Autors.objects.create(name = request.POST['autor'])     # TODO: validate(if author exist!?!?!) typo by user when populate form, make '.to_lower' and strip()
    


        try:
            publisher_exist = Publishers.objects.get(publisher_name=request.POST['publisher'])
            publisher = publisher_exist
        except:
            publisher = Publishers.objects.create(publisher_name = request.POST['publisher'])     # TODO: validate(if author exist!?!?!) typo by user when populate form, make '.to_lower' and compare


        title= request.POST['title']
        description= request.POST['description']
        image1=request.FILES['image']
        genre= request.POST['genre']
        owner = request.user
        year_of_publication=request.POST['year_of_publication']
        
        instance = Books(title=title, description=description, genre=genre, image=image1, owner=owner, autor=autor, publisher=publisher, year_of_publication=year_of_publication)  # , return_date=return_date, borrow_counter=borrow_counter)
        instance.save()      
        
        return redirect('home page')






def book_details(request, pk):
    try:
        book = Books.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return render(request, 'book-does-not-exists.html')

    if book.is_borrow:
        remaining = (book.return_date - datetime.today().date()).days
        context = {'book': book,
                'remaining': remaining,      
        }
    else:
        context = {'book': book} 

    return render(request, 'book-details.html', context=context)



class BookEditView(LoginRequiredMixin, UpdateView):
    model = Books
    fields = ['title', 'description', 'image', 'genre', 'autor', 'publisher', 'year_of_publication']      # TODO: how to update image field
    template_name = 'book-edit.html'
    success_url = reverse_lazy('home page')

    # cloudinary.uploader.destroy(book.image.public_id,invalidate=True)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Books
    fields = '__all__'
    template_name = 'book-delete.html'
    success_url = reverse_lazy('home page')



def my_books(request, pk):
    context = {
        'books': Books.objects.filter(owner=pk).all()
    }
    return render(request, 'my-books.html', context)



def my_borrowed_books(request, pk):
    context = {
        'books': Books.objects.filter(owner=pk, is_borrow=True).all()
        }
    return render(request, 'my-borrowed-books.html', context)



def borrowed_books(request, pk):
    user = LibraryUser.objects.get(pk=pk)
    context = {
        'books': Books.objects.filter(borrower=user.username).all()
        }
    return render(request, 'borrowed-books.html', context)



def book_borrow(request, pk):
    book = Books.objects.get(pk=pk)
    if request.method == 'GET':
        if book.is_borrow == False:
            book.is_borrow = True
            book.borrow_counter += 1
            book.return_date = datetime.now() + timedelta(days=20)
            book.borrower = request.user.username
            book.save()                                     
    return redirect('home page')



def book_returned(request, pk):
    book = Books.objects.get(pk=pk)
    if request.method == 'GET':
            book.is_borrow = False
            book.borrower = None
            book.return_date = None
            book.save()
    return redirect('home page')

