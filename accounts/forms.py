from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm ## When Create newuser or Using Django User Model We Use UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model =User
        fields = ['first_name','last_name','username','email']
        


class DepositeForm(forms.Form):
    amount = forms.DecimalField(max_digits=10,decimal_places=2,min_value=1,required=True,label='Amount',widget=forms.NumberInput(attrs={'placeholder':'Enter Amount'}))
    
    
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']