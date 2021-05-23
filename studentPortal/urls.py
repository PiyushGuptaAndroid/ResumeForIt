from django.urls import path
from studentPortal import views

urlpatterns = [
    path('startquiz', views.startquiz, name='index'),
    path('quiz', views.quiz, name='index'),
    path('endquiz', views.endquiz, name='index'),
    path('loggedInAsStudent', views.studentDashboard, name='index'),
]