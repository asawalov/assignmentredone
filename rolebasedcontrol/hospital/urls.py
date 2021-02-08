from django.urls import path, include
from .models import user_type
from .import views
urlpatterns = [
    path('', views.dashboard,name='dashboard'),
    path('signup/<str:name>/',views.signup,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('doctor/',views.doctor,name='doctor'),
    path('nurse/',views.nurse,name='nurse'),
    path('surgeon/',views.surgeon,name='surgeon'),
    path('doctor/createuserbyd/',views.createuserbyd,name='createuserbyd'),
    path('nurse/createuserbyn/',views.createuserbyn,name='createuserbyn'),
    path('doctor/updateuser/<str:pk>/',views.updateuserbyd,name='updateuser'),
    path('nurse/updateuser/<str:pk>/',views.updateuserbyn,name='updateuser'),
    path('surgeon/updateuser/<str:pk>/',views.updateuserbys,name='updateuser'),
    path('doctor/deleteuser/<str:pk>/',views.deleteuser,name='deleteuser'),
]
