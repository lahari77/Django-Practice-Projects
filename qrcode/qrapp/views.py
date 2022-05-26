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
			image.save('ststic/qrcode/qrcode1.jpg')
			return render(request,'qrcode.html')
		else:
			return HttpResponse("<h1>Invalid Username/Password</h1>")
