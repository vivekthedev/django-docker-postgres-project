from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Book


class BookListView(LoginRequiredMixin,ListView):
    context_object_name = "book_list"
    model = Book
    template_name = "books/book_list.html"
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = 'account_login'
    permission_required = 'books.special_status'

