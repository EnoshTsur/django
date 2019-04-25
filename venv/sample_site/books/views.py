from django.http import HttpResponse, Http404
from django.shortcuts import render
from books.models import Book, Author, Customer

# Create your views here.

books = [
    {'id': 1, 'name': 'harry potter'},
    {'id': 2, 'name': 'Easy Python'},
    {'id': 3, 'name': 'Easy JavaScript'}
]

def index(request):
    return HttpResponse('<h1>hi there books!</h1>')

def genre(request):
    return HttpResponse('<h1>Comedy!!!</h1>')

def get_book(request, index):
    if index >= len(books):
        return HttpResponse(f'No book with the index {index}')
    return HttpResponse(f'{books[index]}')

def by_id(request, index):
    return HttpResponse(f'ID: {index}')

def get_params(request):
    id = request.GET['id']
    name = request.GET.get('name')
    return HttpResponse(f'Params: id-{id} name-{name}')

def get_book_by_id(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404(f'Book with the id {id} does not exists')
    return render(request, 'books/index.html', {'book': book})
