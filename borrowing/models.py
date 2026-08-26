from django.db import models
from accounts.models import UserProfile
from books.models import Book
# Create your models here.

class Borrowing(models.Model):
    ## one user borrow many times, so many(Borrowing) to one(User) relationship, so we use ForeignKey
    user = models.ForeignKey(UserProfile,on_delete = models.CASCADE,related_name='borrowings') ## if user is deleted, all borrowed books will be deleted
    ## if one(user) is deleted , this users row or this user history is deleted,
    ## one book can borrowed many time, so many(Borrowing) to one(Book) relationship, so we use ForeignKey
    book = models.ForeignKey(Book,on_delete = models.CASCADE,related_name='borrowings') ## if book is deleted, all borrowed books will be deleted
    borrowed_at = models.DateTimeField(auto_now_add=True) ## automatically set the field to now when the object is first created.
    returned_at = models.DateField(null=True,blank=True)
    returned = models.BooleanField(default = False)
    ## related_name is used to access the related objects from the other side of the relationship. For example, if you have a UserProfile object, you can access all the borrowed books of that user using user.borrowings.all() and if you have a Book object, you can access all the users who borrowed that book using book.borrowings.all()