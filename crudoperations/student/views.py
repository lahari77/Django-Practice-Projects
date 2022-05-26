from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'student/home.html')

def addstudent(request):
	if request.method=="POST":
		rollno = request.POST.get('rollno')
		name = request.POST.get('name')
		email = request.POST.get('email')
		branch = request.POST.get('branch')
		mobileno = request.POST.get('mobileno')
		Student.objects.create(rollno=rollno,name=name,branch=branch,email=email,mobileno=mobileno)
		messages.success(request,'%s is successfully registered..!'%(name))
		return redirect('showdata')
	return render(request,'student/addstudent.html')

def showdata(request):
	data = Student.objects.all()
	return render(request,'student/showdata.html',{'data':data})

def editstudent(request,id):
	stu = Student.objects.get(id=id)
	if request.method=="POST":
		stu.rollno = request.POST.get('rollno')
		stu.name = request.POST.get('name')
		stu.email = request.POST.get('email')
		stu.branch = request.POST.get('branch')
		stu.mobileno = request.POST.get('mobileno')
		stu.save()
		messages.info(request,'%s is successfully updated..!'%(stu.name))
		return redirect('showdata')
	return render(request,'student/editstudent.html',{'stu':stu})

def deletestudent(request,id):
	studel = Student.objects.get(id=id)
	if request.method=="POST":
		studel.delete()
		messages.warning(request,'%s is successfully deleted..!'%(studel.name))
		return redirect('showdata')
	return render(request,'student/deletestudent.html',{'studel':studel})
