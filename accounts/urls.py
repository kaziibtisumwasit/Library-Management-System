from django.urls import path

from .views import UserRegistrationView,UserLoginView,UserLogout,depositeView,UserProfileUpdate

urlpatterns = [
    path('user-registration/', UserRegistrationView.as_view(), name='user_registration'),
    path('user-login/',UserLoginView.as_view(),name='user_login'),
    path('user-logout/',UserLogout,name='user_logout'),
    path('deposite-amount/',depositeView,name='deposite'),
    path('user-profile/',UserProfileUpdate,name='profile_update'),
]