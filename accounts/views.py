from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import UserProfile
from django.views.generic import CreateView ## Create New object -->> New User Registration 
from django.contrib.auth.views import LoginView,LogoutView ## LoginView and LogoutView are built-in views provided by Django for handling user authentication. They handle the login and logout processes, respectively.
from django.contrib.auth import login,logout ## for FBV
# Create your views here.


class UserRegistrationView(CreateView):## CreateView Automatically handles the form submission and validation, and saves the new user to the database.
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Create New Account'
        context['button_text'] = 'Register'
        return context
    
    
    
# def UserRegistrationView(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = UserrRegistrationForm()
#     return render(request,'register.html',{'form' : form})



class UserLoginView(LoginView):
    template_name = 'registration/register.html'
    
    def get_success_url(self): ## LoginView By defalt rediret on profile url, but we want to redirect on home page after login, so we override get_success_url method
        return reverse_lazy('home')
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'User Login'
        context['button_text'] = 'Login'
        return context



    
    
# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('home') ## LogoutView By defalt rediret on profile url, but we want to redirect on home page after logout, so we override next_page attribute
def UserLogout(request):
    logout(request)
    return redirect('home')