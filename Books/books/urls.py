from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('search/', views.search_books, name='search_books'),
    path('update_status/<int:pk>/', views.update_status, name='update_status'),
]