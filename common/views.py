from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

# from search_views.search import SearchListView
# from search_views.filters import BaseFilter


# from accounts_manage.models import LibraryUser
from books.models import Books
# from common.forms import SearchForm         # BooksSearchForm, 


from django.contrib.auth import get_user_model



UserModel = get_user_model()




class HomePageView(ListView):
    template_name = 'home-page.html'
    model = Books




class SearchResultsView(ListView):
    model = Books
    template_name = "home-page.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Books.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
