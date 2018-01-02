from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import include

from . import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'books/', views.BookListView.as_view(), name='books'),
    path(r'book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    path(r'authors/', views.AuthorListView.as_view(), name='authors'),
    path(r'authors/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path(r'mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'book/<pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path(r'borrowed/', views.BorrowedBooksListView.as_view(), name='borrowed-books'),
    path(r'author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path(r'signup/', views.UserSignup, name='signup'),
]


# Author create, update and delete urls
urlpatterns += [
    path(r'authors/<pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path(r'authors/<pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
