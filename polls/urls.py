from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.get_books, name='get_books'),
    path('add_book/', views.add_book, name='add_book'),
]
