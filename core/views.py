from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book,Category
# Create your views here.



def HomeView(request,category_id=None):
    categories = Category.objects.all()  # Get unique categories from the books
    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
        
    context = {
        'books': books,
        'categories': categories,
    }
    return render(request,'home.html',context)




# class HomeView(ListView): ## list view use -->> because we show all books as list in home page
#     model = Book 
#     template_name = 'home.html'
#     # context_object_name = 'books' ## Book model er data ke books name e access korte parbo forntend e 
#     ## extra context data send korete get_context_data method use korte hobe, jekhane amra categories data o send korbo frontend e
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()  # Get unique categories from the books
#         return context
    