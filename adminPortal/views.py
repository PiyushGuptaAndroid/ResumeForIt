from django.shortcuts import render
from django.http import HttpResponse
from adminPortal.models import Question
from django.core import serializers

# Create your views here.


def loggedInAsAdmin(request):
    return render(request, 'adminPortal/adminDashboard.html')


def addQuestions(request):
    if(request.method == "GET"):
        return render(request, 'adminPortal/addQuestions.html')
    if(request.method == "POST"):
        question = request.POST['question']
        optionA = request.POST['optionA']
        optionB = request.POST['optionB']
        optionC = request.POST['optionC']
        optionD = request.POST['optionD']
        correctOption = request.POST['correctOption']
        tag = request.POST['tag']
        data = Question(question=(question + ' ?'), optionA=optionA, optionB=optionB,
                        optionC=optionC, optionD=optionD, correctOption=correctOption, tag=tag)
        data.save()
        return render(request, 'adminPortal/addQuestions.html')


def adminDashboard(request):
    tags = Question.objects.values('tag').distinct()
    print(tags)
    return render(request, 'adminPortal/adminDashboard.html', {'tags': tags})


def eligibleCandidates(request):
    return render(request, 'adminPortal/eligibleCandidates.html')


def registerAdmins(request):
    return render(request, 'adminPortal/registerAdmins.html')

def questions(request, tag):
    print(tag)
    ques_dict = Question.objects.filter(tag = tag )
    print(ques_dict)
    return render(request, 'adminPortal/questions.html', {'ques_dict' : ques_dict})
