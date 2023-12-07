from django.db import models

# Create your models here.
class donations(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    food_type=models.TextField()
    quantity=models.IntegerField()
    address=models.TextField()
    
    