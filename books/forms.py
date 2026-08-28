from django import forms
from .models import Book,Category,UserReview



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description","category", "image", "borrowing_price",]
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 focus:border-blue-500 '
                         'outline-none transition',
                'placeholder': 'Enter book title',
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 focus:border-blue-500 '
                         'outline-none transition resize-none',
                'rows': 5,
                'placeholder': 'Write a short description...',
            }),

            'category': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 focus:border-blue-500 '
                         'outline-none transition bg-white',
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'bg-gray-50 cursor-pointer',
            }),

            'borrowing_price': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 focus:border-blue-500 '
                         'outline-none transition',
                'placeholder': 'Enter borrowing price',
                'step': '0.01',
            }),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        
        widgets = {
                    'name': forms.TextInput(attrs={
                        'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                                 'focus:ring-2 focus:ring-blue-500 focus:border-blue-500 '
                                 'outline-none transition',
                        'placeholder': 'Enter category name',
                    }),
                    'description': forms.Textarea(attrs={
                        'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                                 'focus:ring-2 focus:ring-blue-500 focus:border-blue-500 '
                                 'outline-none transition resize-none',
                        'rows': 5,
                        'placeholder': 'Write a description...',
                    }),
            }
        
        
class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ["review_text"] ## ONLY REVIEW TEXT IS REQUIRED FROM USER, BOOK AND USER WILL BE AUTOMATICALLY ADDED IN VIEWS.PY
        
        widgets = {
            'review_text' : forms.Textarea(attrs={
                'class' : 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition resize-none',
                'rows' : 5,
                'placeholder' : 'Write your review here...'
            }) 
        } 