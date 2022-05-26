from django.db import models

# Create your models here.

class Parent(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()

	def __str__(self):
		return self.name+" "+self.age

class Children(Parent,models.Model):
	
	name = models.CharField(max_length=20)
	gender = models.CharField(max_length=6)
