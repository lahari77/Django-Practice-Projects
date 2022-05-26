from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("upload",views.send_files,name="uploads"),
    ]
