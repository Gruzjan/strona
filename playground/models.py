from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    number = models.IntegerField()
    
class Class(models.Model):
    name = models.CharField(max_length=20)
    
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    
    