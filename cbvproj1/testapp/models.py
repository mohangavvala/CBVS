from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=64)
    author=models.CharField(max_length=64)
    price=models.FloatField()
    pages=models.IntegerField()