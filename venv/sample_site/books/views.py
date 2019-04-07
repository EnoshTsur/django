from django.http import HttpResponse
from django.shortcuts import render

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