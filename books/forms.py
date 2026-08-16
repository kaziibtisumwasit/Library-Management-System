from django import forms
from .models import Book,Category



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description","category", "image", "borrowing_price", "user_review"]
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]