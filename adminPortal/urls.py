from django.urls import path
from adminPortal import views

urlpatterns = [
    path('loggedInAsAdmin', views.loggedInAsAdmin, name='index'),
    path('addQuestions', views.addQuestions, name='index'),
    path('adminDashboard', views.adminDashboard, name='index'),
    path('eligibleCandidates', views.eligibleCandidates, name='index'),
    path('registerAdmins', views.registerAdmins, name='index'),
]