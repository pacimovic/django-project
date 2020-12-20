from django.db import models

# Create your models here.

class Food(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField()
    desc = models.TextField()
    price = models.IntegerField()
