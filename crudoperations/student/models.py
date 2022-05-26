from django.db import models

# Create your models here.
class Student(models.Model):
	
	rollno = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	branch = models.CharField(max_length=20)
	email = models.EmailField(max_length=20)
	mobileno = models.CharField(max_length=12)