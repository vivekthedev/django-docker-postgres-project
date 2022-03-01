from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    context_object_name = "book_list"
    model = Book
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
