from django.urls import path

from .views import home,internal,external

urlpatterns = [
	path('',home),
	path('internal',internal),
	path('external',external),
	]