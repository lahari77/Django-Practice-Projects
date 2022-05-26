

from django.urls import path

from.views import home,addmovie,showmovies,editmovie,sendmail,register,profile,updateprofile

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('',home,name="home"),

	path('addmovie',addmovie,name="addmovie"),
	path('showmovies',showmovies,name="showmovies"),
	path('editmovie/<int:id>',editmovie,name="editmovie"),
	path('sendmail',sendmail,name="sendmail"),
	path('register',register,name="register"),
	path('login',auth_views.LoginView.as_view(template_name='movies/login.html'),name="login"),
	path('logout',auth_views.LogoutView.as_view(template_name='movies/logout.html'),name="logout"),
	path('profile',profile,name="profile"),
	path('updateprofile',updateprofile,name="updateprofile"),

	]
