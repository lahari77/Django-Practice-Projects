from django.db import models

# Create your models here.

class Student(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	branch = models.CharField(max_length=5)

	def __str__(self):
		return self.firstname+" "+self.lastname+" "+self.branch