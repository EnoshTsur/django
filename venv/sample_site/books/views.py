from django.http import HttpResponse, Http404
# new get or http404
from django.shortcuts import render, get_object_or_404 
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

# new
def submit(request):
    name = request.POST['name']
    genre = request.POST['genre']
    author_id = request.POST['author']
    
    author = Author.objects.get(pk=author_id)
    book = Book(name=name, genre=genre, author=author)
    book.save()
    books = Book.objects.all()

    return render(request, 'books/create.html', {'books': books})
    
# new
def create_book(request):
    books = Book.objects.all()
    return render(request, 'books/create.html', {'books': books})

# new 
def get_author_by_id(request, id):
    author = get_object_or_404(Author, pk=id)
    return render(request, 'books/author.html', {'author': author})