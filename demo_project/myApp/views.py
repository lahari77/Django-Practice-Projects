from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Welcome to the home page")
def about(request):
	return HttpResponse("Welcome to the about page.<h2><i>I'm Lahari<h2>")
def name(req,name):
	return HttpResponse("Hi I'm "+name)
def rollno(req,roll):
	return HttpResponse("Welcome roll "+str(roll))
def student(req,name,roll):
	return HttpResponse("Hi I'm {}. My rollno is {}".format(name,roll))