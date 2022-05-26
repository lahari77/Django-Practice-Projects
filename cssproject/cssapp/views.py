from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'cssapp/home.html')

def internal(request):
	return render(request,'cssapp/internal.html')
	
def external(request):
	return render(request,'cssapp/external.html')