from django.shortcuts import render
from django.http import HttpResponse
import random
import qrcode
# Create your views here.

otp = 0
def login(request):

	return render(request,'login.html')

def validatelogin(request):
	if request.method=="POST":
		username = request.POST.get("t1")
		password = request.POST.get("t2")
		if username=="lahari77" and password=="Admin@577":
			rno = random.randint(1000,9999)
			global otp
			otp  =rno
			image = qrcode.make("Otp: "+str(otp))
			image.save('myapp/static/qrcode1.jpg')
			return render(request,'code.html')
		else:
			return HttpResponse("<h1>Invalid Username/Password</h1>")

def validateotp(request):
	if request.method=="POST":
		userotp = request.POST.get('uotp')
		if userotp==str(otp):
			name="Lahari"
			age=20
			gender="Female"
			image2=qrcode.make("Name: "+name+"\n"+"Age: "+str(age)+"\n"+"Gender: "+gender)
			image2.save('myapp/static/qrcode2.jpg')
			return render(request,'welcome.html')
		else:
			return HttpResponse("Wrong OTP")
