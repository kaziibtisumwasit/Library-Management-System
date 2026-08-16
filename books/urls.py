from django.urls import path
from .views import addBook,addCategory



urlpatterns = [
    path('add-book/', addBook, name="add_book"),
    path('add-category/', addCategory, name="add_category"),
    
]