from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # Connect the UserProfile model to the built-in User model using a OneToOneField
    user = models.OneToOneField(User,on_delete=models.CASCADE) ## One user has one profile, if user is deleted User Profile will be deleted 
    balance = models.DecimalField(max_digits= 10, decimal_places=2, default=0.00)
    
    
    def __str__(self):
        return self.user.username
    