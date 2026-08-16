from django.urls import path

from .views import UserRegistrationView,UserLoginView,UserLogout

urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('user-login/',UserLoginView.as_view(),name='user_login'),
    path('user-logout/',UserLogout,name='user_logout')
]