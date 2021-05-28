from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
   path('adminLogin/', views.adminLogin, name="alogin"),
   path('adlogout/', views.adlogoutUser, name="adlogout"),
   path('open/',views.open,name="open"),
]