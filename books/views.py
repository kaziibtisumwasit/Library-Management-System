from django.shortcuts import render,redirect
from .forms import BookForm,CategoryForm

# Create your views here.



def addBook(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES) ## POST --> text data, FILES --> image data
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request , "add_book.html",{'form' : form , 'title' : 'Book'})



def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request,'add_book.html',{'form':form, 'title' : 'Category'})