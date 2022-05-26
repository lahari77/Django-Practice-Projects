from django.urls import path

from .views import home,addstudent,showdata,editstudent,deletestudent
urlpatterns = [
path('',home,name="home"),
path('addstudent',addstudent,name="addstudent"),
path('showdata',showdata,name="showdata"),
path('editstudent/<int:id>',editstudent,name="editstudent"),
path('deletestudent/<int:id>',deletestudent,name="deletestudent"),
]