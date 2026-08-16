from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm ## When Create newuser or Using Django User Model We Use UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model =User
        fields = ['first_name','last_name','username','email']
        
