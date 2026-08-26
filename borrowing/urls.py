from django.urls import path,include
from .views import borrowing_book,borrowingHistory


urlpatterns = [
    path('borrowing/<int:pk>/' , borrowing_book, name='borrow_book'),
    path('borrowing-history/',borrowingHistory,name='borrowing_history'),
    
]