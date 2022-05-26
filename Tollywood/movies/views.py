from django.shortcuts import render,redirect

from.forms import MovieForm,RegisterForm,UpdateRegisterForm,UpdateProfileForm

from.models import Movie,UserProfile

from django.contrib.auth.models import User

from django.contrib import messages

from django.http import HttpResponse

from Tollywood import settings

from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,'movies/home.html')

@login_required
def addmovie(request):
	if request.method=="POST":
		form = MovieForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'Movie is successfully added..!')
			return HttpResponse('done')
	else:
		form = MovieForm()
		return render(request,'movies/addmovie.html',{'form':form})


def showmovies(request):
	data = Movie.objects.all()
	return render(request,'movies/showmovies.html',{'data':data})

@login_required
def editmovie(request,id):
	movieedit = Movie.objects.get(id=id)
	if request.method=="POST":
		form=MovieForm(request.POST,request.FILES,instance=movieedit)
		if form.is_valid():
			form.save()
			messages.warning(request,'successfully Updated..!')
			return redirect('showmovies')
	form = MovieForm(instance=movieedit)
	return render(request,'movies/editmovie.html',{'form':form,'movieedit':movieedit})

@login_required
def sendmail(request):
	if request.method=="POST":
		to = request.POST.get('to')
		sub =request.POST.get('subject')
		body=request.POST.get('body')
		sender = settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[to])
		messages.success(request,'%s is successfully sent'%(to))
		return redirect('/')
	return render(request,'movies/sendmail.html')

def register(request):
	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"Successfully Registered..!")
			return redirect('login')
	else:
		form = RegisterForm()
		return render(request,'movies/register.html',{'form':form})

def profile(request):
	user= User.objects.get(id=request.user.id)
	pro = UserProfile.objects.get(user=user)
	context={'user':user,'pro':pro}
	return render(request,'movies/profile.html',context)

def updateprofile(request):
	if request.method=="POST":
		u_form=UpdateRegisterForm(request.POST,instance=request.user)
		p_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
		# if u_form.is_valid() and p_form.is_valid():
		u_form.save()
		p_form.save()
		messages.success(request,"profile Successfully Updated..!")
		return render(request,'movies/profile.html')
	else:
		u_form = UpdateRegisterForm(instance=request.user)
		p_form = UpdateProfileForm(instance=request.user.userprofile)
		context = {'u_form':u_form,'p_form':p_form}
		return render(request,'movies/updateprofile.html',context)
