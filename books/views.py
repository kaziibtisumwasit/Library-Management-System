from django.shortcuts import render,redirect
from .forms import BookForm,CategoryForm,UserReviewForm
from django.views.generic import DetailView
from .models import Book,Category,UserReview
from borrowing.models import Borrowing
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='user_login') ## login_required decorator is used to restrict access to the view for authenticated users only. If an unauthenticated user tries to access this view, they will be redirected to the login page specified by the login_url parameter.
def addBook(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) ## POST --> text data, FILES --> image data
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request , "add_book.html",{'form' : form , 'title' : 'New Book','button_text' : 'Add Book'})



@login_required
def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request,'add_book.html',{'form':form, 'title' : 'Add New Category','button_text' : 'Add Category'})

# class bookDetails(DetailView): ## IN CBV on DetailView Automatically pass the object id
#     model = Book
#     template_name = 'book_details.html'
#     context_object_name = 'book' ## By default, the context variable name for the object in a DetailView is 'object'. However, you can customize it by setting the context_object_name attribute. In this case, we set it to 'book', so in the template, you can access the book object using {{ book }} instead of {{ object }}.
    
    
# class UserReviewView(DetailView):
#     pass


@login_required
def bookDetails(request,pk):
    book = Book.objects.get(pk=pk) ## get the current book object using pk
    
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            if UserReview.objects.filter(book=book,user=request.user).exists():
                form.add_error(None,"You Are Already Reviewed This Book") ## add error to the form if the user has already reviewed the book
            elif not Borrowing.objects.filter(book=book,user=request.user.userprofile).exists():
                form.add_error(None,"You Can Only Review This Book If You Borrowed It") ## add error to the form if the user has not borrowed the book
                
            else:
                review = form.save(commit=False) ## Create a new UserReview instance but didn't save it to the database yet
                review.book = book ## Assign the current book object to the book field of the UserReview instance
                review.user = request.user ## Assign the current logged-in user to the user field of the UserReview instance
                review.save() ## Save the UserReview instance to the database
 
    else:
        form = UserReviewForm()
    
    reviews = book.reviews.all() ## get all the reviews of the current book object using related_name 'reviews' in UserReview model
    return render(request,'book_details.html',{'book':book,'reviews':reviews,'form':form}) ## pass the current book object, all reviews of the current book object and the review
            
            
            



