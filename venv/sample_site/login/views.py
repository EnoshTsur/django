from django.shortcuts import render, get_object_or_404

def login_page(request):
    return render(request, 'login/index.html', {})

def submit(request):
    name = request.POST['name']
    pwd = request.POST['password']
    isAuthor = request.POST['isAuthor']
    print(name)
    print(pwd)
    print(isAuthor)
    if isAuthor == 'on':
        return render(request, 'books/author.html', {})
    else:
        return render(request, 'books/index.html', {})
    return None