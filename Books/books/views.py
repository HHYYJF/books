from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def book_list(request): # отобродение всех записей
    books = Book.objects.all()
    return render(request, 'blog/book_list.html', {'books': books})

def add_book(request): # создание записей
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'blog/add_book.html', {'form': form})

def delete_book(request, pk): # фильтр книг и получение 1й get_object_or_404 если нет обьекта то будет 404 (обработка ошибок)
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def search_books(request): # фильтр книг по критериям
    query = request.GET.get('q')
    books = Book.objects.filter(
        title__icontains=query
    ) | Book.objects.filter(
        author__icontains=query
    ) | Book.objects.filter(
        year__icontains=query
    )
    return render(request, 'blog/book_list.html', {'books': books, 'query': query})

def update_status(request, pk): # изменение книги
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Book.STATUS_CHOICES):
            book.status = new_status
            book.save()
            return redirect('book_list')
    return render(request, 'blog/update_status.html', {'book': book})
