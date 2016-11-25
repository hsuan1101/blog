from django.shortcuts import render

from book.models import Book

# Create your views here.

def book(request):
    books = Book.objects.all()
    return render(request, 'book/book.html', {'books':books})