from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    
    title = models.CharField(max_length=255)
    descreption = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_availible = models.BooleanField(default=False)

    def __str__(self):
        return self.title
