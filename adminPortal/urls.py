from django.urls import path
from adminPortal import views

urlpatterns = [
    path('loggedInAsAdmin', views.loggedInAsAdmin, name='index'),
]