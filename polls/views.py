from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_books(request):
    # Dummy data for demonstration purposes
    books = ['Book 1', 'Book 2', 'Book 3']
    return JsonResponse({'books': books})


@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        # Extract book title from the request body
        book_title = request.POST.get('title', '')  # Assuming 'title' is the key for the book title

        return JsonResponse({'message': f'Book "{book_title}" added successfully!'})
    else:
        # Render a form for adding a new book
        return render(request, 'add_book.html')
