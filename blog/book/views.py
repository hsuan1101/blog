from django.shortcuts import render

from book.models import Book

# Create your views here.

def book(request):
    '''
    Render the book page
    '''
    books = Book.objects.all()
    itemsList = []
    for book in books:
        items = [book]
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'book/book.html',context)
