
from ast import pattern
from django import urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# from django.conf import settings #add this
# from django.conf.urls.static import static #add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('accounts/', include('accounts_manage.urls')),
    path('books/', include('books.urls')),
    path('forum/', include('forum.urls'))
] 

handler500='common.exceptions_handlers.handler_server_error'




# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

