from django.urls import path

from.views import home,train_or_predict

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',home,name="home"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'),name="login"),
	path('train_or_predict/',train_or_predict,name="train_or_predict"),
	# path('train/',train,name="train"),
	# path('predict/',predict,name="predict"),
	path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
	
	]