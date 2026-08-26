from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,DepositeForm
from .models import UserProfile
from django.views.generic import CreateView ## Create New object -->> New User Registration 
from django.contrib.auth.views import LoginView,LogoutView ## LoginView and LogoutView are built-in views provided by Django for handling user authentication. They handle the login and logout processes, respectively.
from django.contrib.auth import authenticate,login,logout ## for FBV
from utils.email import sending_email ## for sending email after user registration



# Create your views here.


class UserRegistrationView(CreateView):## CreateView Automatically handles the form submission and validation, and saves the new user to the database.
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self,form):##on form validation time or before form.save()
        response = super().form_valid(form)
        ## in UserProfile model on user object we put into current registered user, so we can access the current logged in user profile using request.user.userprofile 
        UserProfile.objects.create(user=self.object) ## current registered user link into UserProfile Model,
        ## UserProfile Model e Current Registered User er jonno ekta object create korlam, jate kore user registration er por automatically user profile create hoye jai.
        # sending_email(self.object,'Registration Successful','registration/email_registration.html') ## send email after user registration
        login(self.request,self.object)
        return response
        
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Create New Account'
        context['button_text'] = 'Register'
        return context
    
    
    
# def UserRegistrationView(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             UserProfile.objects.create(user=user) ## Create UserProfile object for the newly registered user
#             login(request,user) ## Automatically log in the user after successful registration
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
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
    
# def UserLoginView(request):
#     if request.method == 'POST':
#         username = request.POST.get('username') ## get data from template username field and password field and authenticate the user using authenticate() function. If the user is authenticated, we log them in using login() function and redirect them to home page. If the user is not authenticated, we display an error message on the login page.
#         password = request.POST.get('password')

#         user = authenticate(
#             request,
#             username=username,
#             password=password
#         )

#         if user is not None:
#             login(request, user)
#             return redirect('home')

#         context = {
#             'error_message': 'Invalid username or password'
#         }
#         return render(request, 'registration/login.html', context)

#     return render(request, 'registration/login.html')

    
    
# class UserLogoutView(LogoutView):
#     next_page = reverse_lazy('home') ## LogoutView By defalt rediret on profile url, but we want to redirect on home page after logout, so we override next_page attribute
def UserLogout(request):
    logout(request)
    return redirect('home')



def depositeView(request):
    if request.method == 'POST':
        form = DepositeForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_profile = UserProfile.objects.get(user=request.user) ## current logged user
            user_profile.balance += amount
            user_profile.save()
            # sending_email(request.user,'Deposite Successful','registration/email_deposite.html') ## send email after deposite
            return redirect('home')
            
    else:
        form = DepositeForm()
        context = {
            'title' : 'Deposite Money',
            'button_text' : 'Deposite',
            'form' : form
        }
        return render(request, 'registration/register.html', context)