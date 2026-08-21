from django import forms
from .models import Book,Category,UserReview



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description","category", "image", "borrowing_price",]
        
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        
        
class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ["review_text"] ## ONLY REVIEW TEXT IS REQUIRED FROM USER, BOOK AND USER WILL BE AUTOMATICALLY ADDED IN VIEWS.PY