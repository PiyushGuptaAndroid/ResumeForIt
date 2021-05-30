from django.urls import path
from studentPortal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('startquiz', views.startquiz, name='index'),
    path('quiz', views.quiz, name='index'),
    path('endquiz', views.endquiz, name='index'),
    path('studentDashboard', views.studentDashboard, name='index'),
    path('studentRegistration', views.studentRegistration, name='index'),
    path('studentProfile', views.studentProfile, name='index'),
    path('studentAnalysis', views.studentAnalysis, name='index'),
    path('gettingResult', views.gettingResult, name='index'),
    path('uploadResume', views.uploadResume, name='index'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)