from django.shortcuts import render

# Create your views here.
def home(request):
	data = ["Jughead","Archie","Betty","Veronica"]
	return render(request,'home.html',{'req':data})
def home1(request):
	l1=[]
	for i in range(1,6):
		l1.append(i)
	return render(request,'check.html',{'n':l1})
def table(req,num):
	data=[]
	for i in range(1,11):
		tab=str(num)+" * " + str(i) + " = "+str(num*i)
		data.append(tab)
	return render(req,'table.html',{'data':data})
def tabular(request):
	return render(request,'tabular.html')
def register(request):
	if request.method=="POST":
		a=request.POST['uname']
		b=request.POST['uage']
		c=request.POST['unumber']
		data = {'Name':a,'Age':b,'Mobile':c}
		return render(request,'details.html',{'info':data})
	return render(request,'register.html')

