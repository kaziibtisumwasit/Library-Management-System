from django.contrib import admin
from .models import Book,Category,UserReview
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(UserReview)