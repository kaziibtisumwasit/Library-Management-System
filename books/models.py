from django.db import models
from accounts.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name = 'books')
    ## many books in one category, so we use ForeignKey here, ManyToOne realationship, related_name = 'books' means we can access all books in a category using category.books.all()
    ## On_delete=models.CASCADE means if a category is deleted, all books in that category will be deleted too.
    image = models.ImageField(upload_to="books/images/")
    borrowing_price = models.DecimalField(max_digits=6, decimal_places=2)
    # user_review = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    
class UserReview(models.Model):
    ## one book has many reviews, if a book delete that book review will be deleted
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name = 'reviews') ## many reviews in one book, so we use ForeignKey here, ManyToOne realationship, related_name = 'reviews' means we can access all reviews in a book using book.reviews.all()
    ## one user can do many book review , current use can access all his review using related_name . my_review
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'my_reviews') ## many book reviews by one user, so we use ForeignKey here, ManyToOne realationship, related_name = 'reviews' means we can access all reviews by a user using user.reviews.all()
    review_text = models.TextField()
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"

class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    