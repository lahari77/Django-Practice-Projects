from django.shortcuts import render

# Create your views here.
def home(request):
	if request.method=="POST":
		t1button = request.POST.get("team1")
		t2button = request.POST.get("team2")
		if t1button is not None:
			t1 = int(request.POST.get('t1'))+1
			t2 = int(request.POST.get('t2'))
		else:
			t1 = int(request.POST.get('t1'))
			t2 = int(request.POST.get('t2'))+1
		return render(request,'scoreboard.html',{'t1':t1,'t2':t2})
	return render(request,'scoreboard.html')