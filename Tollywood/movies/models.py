from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(default="default.png",upload_to="profilepics")
	dob = models.DateField(null=True,blank=True)
	age=models.IntegerField(default=18)
	mobileno = models.CharField(max_length=10)

@receiver(post_save,sender=User)
def createprofile(sender,instance,created,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)






class Movie(models.Model):



	actors = [('Balakrishna','Balakrishna'),('Jr.Ntr','Jr.Ntr'),('MaheshBabu','MaheshBabu'),
	('Prabhas','Prabhas')]

	actress = [('Anushka','Anushka'),('Kajal ','Kajal'),('Samantha','Samantha'),
	('Rakul','Rakul')]

	title_name = models.CharField(max_length=30)
	poster = models.ImageField(upload_to='posters')
	actor_name = models.CharField(max_length=20, choices=actors, default='Missing')
	actress_name = models.CharField(max_length=20, choices=actress, default='Missing')
	trailer = models.FileField(upload_to='trailers')

