from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'main/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'main/add_book.html', {'form': form})

def toggle_favorite(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.is_favorite = not book.is_favorite
    book.save()
    return redirect('book_list')
