from django.shortcuts import render
from django.http import HttpResponse
from adminPortal.models import Question

# Create your views here.


def loggedInAsAdmin(request):
    return render(request, 'adminPortal/adminDashboard.html')


def addQuestions(request):
    print(request.method)
    if(request.method == "GET"):
        print("get method")
        return render(request, 'adminPortal/addQuestions.html')
    if(request.method == "POST"):
        print("post method")
        print(request.POST)
        question = request.POST['question']
        optionA = request.POST['optionA']
        optionB = request.POST['optionB']
        optionC = request.POST['optionC']
        optionD = request.POST['optionD']
        correctOption = request.POST['correctOption']
        tag = request.POST['tag']
        print(question, optionA, optionB, optionC, optionD, correctOption, tag)
        data = Question(question=question, optionA=optionA, optionB=optionB,
                        optionC=optionC, optionD=optionD, correctOption=correctOption, tag=tag)
        data.save()
        print("the data is saved")
        return render(request, 'adminPortal/addQuestions.html')


def adminDashboard(request):
    return render(request, 'adminPortal/adminDashboard.html')


def eligibleCandidates(request):
    return render(request, 'adminPortal/eligibleCandidates.html')


def registerAdmins(request):
    return render(request, 'adminPortal/registerAdmins.html')
