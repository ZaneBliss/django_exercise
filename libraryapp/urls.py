from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('books/form', book_form, name='book_form'),
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('libraries/form', library_form, name='libraries_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout')
]