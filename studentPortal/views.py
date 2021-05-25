from django.shortcuts import render
from django.http import HttpResponse
from adminPortal.models import Question
from json import dumps
from django.core import serializers


# Create your views here.
def startquiz(request):
    return render(request, 'studentPortal/quiz/start.html')


def quiz(request):
    ques = serializers.serialize(
        "json", Question.objects.filter(tag__in=['C++', 'Python']).order_by('?')[:4])
    print()
    questionsJson = dumps(ques)
    return render(request, 'studentPortal/quiz/quiz.html', {'questionsData': questionsJson})


def endquiz(request):
    return render(request, 'studentPortal/quiz/end.html')


def studentDashboard(request):
    return render(request, 'studentPortal/studentDashboard.html')
