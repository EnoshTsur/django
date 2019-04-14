from django.db import models

# Create your models here.
class Author(models.Model):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Author name: {self.name}'

class Customer(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}'

class Book(models.Model):
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    customers = models.ManyToManyField(Customer)
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return f'Name: {self.name} , Genre: {self.genre}'

