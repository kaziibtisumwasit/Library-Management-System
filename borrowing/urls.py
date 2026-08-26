from django.urls import path,include
from .views import borrowing_book


urlpatterns = [
    path('borrowing/<int:pk>/' , borrowing_book, name='borrow_book')
]