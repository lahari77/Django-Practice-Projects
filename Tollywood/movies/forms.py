from django import forms #from django.forms import ModelForm

from .models import Movie,UserProfile

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields=['first_name','last_name','username','email','password1','password2']


class UpdateRegisterForm(forms.ModelForm):
	class Meta:
		model = User

		fields = ['first_name','last_name','email']

class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile

		fields = ['image','dob','age','mobileno']
		
class MovieForm(forms.ModelForm):

	class Meta:

		model = Movie

		fields = '__all__' #['ititle_name','actor_name']




		