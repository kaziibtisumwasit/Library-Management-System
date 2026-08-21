from django.urls import path
from .views import addBook,addCategory,bookDetails



urlpatterns = [
    path('add-book/', addBook, name="add_book"),
    path('add-category/', addCategory, name="add_category"),
    path('book-details/<int:pk>/',bookDetails,name='book_details'),
    
]