from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def startquiz(request):
    return render(request, 'studentPortal/quiz/start.html')

def quiz(request):
    return render(request, 'studentPortal/quiz/quiz.html')

def endquiz(request):
    return render(request, 'studentPortal/quiz/end.html')

def studentDashboard(request):
    return render(request, 'studentPortal/studentDashboard.html')

