from django.shortcuts import render,redirect
from .models import Borrowing
from accounts.models import UserProfile
from books.models import Book
# Create your views here.


def borrowing_book(request,pk):
    selected_book = Book.objects.get(pk = pk) ## get the current book object using pk
    current_user = request.user.userprofile ## get the current logged-in user profile object using request.user.userprofile
    if current_user.balance >= selected_book.borrowing_price : ## check if the current user has enough balance to borrow the book
        current_user.balance -= selected_book.borrowing_price ## from current_user.balance - seloected_book.price = availavle balance is store into current_user.balance
        current_user.save() ## after minus book price , available balance value save into current user profile
        Borrowing.objects.create(
            user = current_user,
            book = selected_book
        )
        return redirect('home') ## after borrowing book redirect to home page
    else:
        return redirect('deposite') ## if current user balance is less than book price then redirect to deposite page