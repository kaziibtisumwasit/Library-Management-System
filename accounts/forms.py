from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm ## When Create newuser or Using Django User Model We Use UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                     'focus:ring-2 focus:ring-blue-500 '
                     'focus:border-blue-500 outline-none transition',
            'placeholder': 'Enter your email address',
        })
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                     'focus:ring-2 focus:ring-blue-500 '
                     'focus:border-blue-500 outline-none transition',
            'placeholder': 'Enter password',
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                     'focus:ring-2 focus:ring-blue-500 '
                     'focus:border-blue-500 outline-none transition',
            'placeholder': 'Confirm password',
        })
    )


    class Meta:

        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

        widgets = {

            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 '
                         'focus:border-blue-500 outline-none transition',
                'placeholder': 'Enter your first name',
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 '
                         'focus:border-blue-500 outline-none transition',
                'placeholder': 'Enter your last name',
            }),

            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'focus:ring-2 focus:ring-blue-500 '
                         'focus:border-blue-500 outline-none transition',
                'placeholder': 'Choose a username',
            }),
        }   


class DepositeForm(forms.Form):

    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=1,
        required=True,
        label='Amount',

        widget=forms.NumberInput(
            attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 '
                         'bg-white text-gray-900 '
                         'focus:outline-none focus:ring-2 '
                         'focus:ring-blue-500 focus:border-blue-500 '
                         'transition',

                'placeholder': 'Enter amount to deposit',

                'step': '0.01',
            }
        )
    )
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
        
        
        
        
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg '
                     'border border-gray-300 '
                     'bg-white text-gray-900 '
                     'focus:outline-none '
                     'focus:ring-2 focus:ring-blue-500 '
                     'focus:border-blue-500 '
                     'transition',
            'placeholder': 'Enter your username',
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg '
                     'border border-gray-300 '
                     'bg-white text-gray-900 '
                     'focus:outline-none '
                     'focus:ring-2 focus:ring-blue-500 '
                     'focus:border-blue-500 '
                     'transition',
            'placeholder': 'Enter your password',
        })
    )