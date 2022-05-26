from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'home.html') 

def train_or_predict(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        print("username : {}".format(username))
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("<h3>You are neither admin nor employee. Please check your credentials and try again.<h3>")
        print("user : {}".format(user))
        print(user.is_superuser)
        if user.is_superuser:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return render(request,'train.html')
            else:
                return HttpResponse("Wrong Password")
        else:
            return render(request,'predict.html')
