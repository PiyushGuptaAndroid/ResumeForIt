from django.shortcuts import render
from django.http import HttpResponse
from adminPortal.models import Question
from login.models import Recruiter
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
    admin_details = Recruiter.objects.get(username = request.session.get('user'))
    tags = Question.objects.values('tag').distinct()
    dict = {
        'admin_details' : admin_details,
        'tags' : tags
    }
    return render(request, 'adminPortal/adminDashboard.html', {'admin_dict': dict})


def eligibleCandidates(request):
    return render(request, 'adminPortal/eligibleCandidates.html')


def registerAdmins(request):
    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        data = Recruiter(username = username, email = email, password = password)
        data.save()
    return render(request, 'adminPortal/registerAdmins.html')

def questions(request, tag):
    ques_dict = Question.objects.get(tag = tag )
    return render(request, 'adminPortal/questions.html', {'ques_dict' : ques_dict})


def editQuestion(request, qid):
    if(request.method == "GET"):
        question_details = Question.objects.get(id = qid)
        return render(request, 'adminPortal/editQuestions.html', {'ques_details' : question_details})
    if(request.method == "POST"):
        question = request.POST['question']
        optionA = request.POST['optionA']
        optionB = request.POST['optionB']
        optionC = request.POST['optionC']
        optionD = request.POST['optionD']
        correctOption = request.POST['correctOption']
        tag = request.POST['tag']
        Question.objects.filter(id = qid).update(question = question, optionA=optionA, optionB=optionB,
                        optionC=optionC, optionD=optionD, correctOption=correctOption, tag=tag)
        question_details = Question.objects.get(id = qid)
        return render(request, 'adminPortal/editQuestions.html', {'ques_details' : question_details})
