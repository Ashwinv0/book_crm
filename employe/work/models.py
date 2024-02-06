from django.db import models

# Create your models here.
class Employe(models.Model):
    email=models.EmailField(null=True)
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    place=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)



class Emp(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=20)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=30)

class Book(models.Model):
    title=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=20)
    place=models.CharField(max_length=35)