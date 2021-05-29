from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, request
from adminPortal.models import Question
from studentPortal.models import User_Profile, Analysis, Resume
from json import dumps
from django.core import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import datetime
import json
from pyresparser import ResumeParser


# importing uuid
import uuid

# Create your views here.

# test = 0
filtered_skills = []

def startquiz(request):
    user = User.objects.get(id= request.user.id)
    resume_data = Resume.objects.get(user_id = user)
    resume_url = '.' + resume_data.resume.url
    filtered_resume = ResumeParser(resume_url).get_extracted_data()
    global filtered_skills
    filtered_skills = filtered_resume['skills']
    return render(request, 'studentPortal/quiz/start.html')


def quiz(request):
    ques = serializers.serialize(
        "json", Question.objects.filter(tag__in=filtered_skills).order_by('?')[:4])
    print()
    questionsJson = dumps(ques)

    return render(request, 'studentPortal/quiz/quiz.html', {'questionsData': questionsJson})


def endquiz(request):
    return render(request, 'studentPortal/quiz/end.html')


def studentDashboard(request):
    # global test
    # test = uuid.uuid4()
    # geek_object = MyUUIDModel.objects.create(id=test)
    # geek_object.save()
    # print(geek_object)
    # print("uuid is saved")
    return render(request, 'studentPortal/studentDashboard.html')


def studentRegistration(request):
    if(request.method == "POST"):
        # print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        DOB = request.POST['DOB']
        phone = request.POST['phone']
        StreetAddress = request.POST[
            'StreetAddress']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        highestDegree = request.POST['highestDegree']
        yearOfDegreeCompleted = request.POST['yearOfDegreeCompleted']
        institution = request.POST['institution']
        specification = request.POST['specification']
        # print(test)
        user = User.objects.get(id= request.user.id)
        if(User_Profile.objects.filter(user_id = user).exists):
            User_Profile.objects.filter(user_id = user).update(
            user_id= user,
            name=name,
            email=email,
            DOB=DOB,
            phone=phone,
            StreetAddress=StreetAddress,
            city=city,
            state=state,
            country=country,
            pincode=pincode,
            highestDegree=highestDegree,
            yearOfDegreeCompleted=yearOfDegreeCompleted,
            institution=institution,
            specification=specification,)
        else :
            data = User_Profile(
                user_id= user,
                name=name,
                email=email,
                DOB=DOB,
                phone=phone,
                StreetAddress=StreetAddress,
                city=city,
                state=state,
                country=country,
                pincode=pincode,
                highestDegree=highestDegree,
                yearOfDegreeCompleted=yearOfDegreeCompleted,
                institution=institution,
                specification=specification,)
            data.save()
    return render(request, 'studentPortal/studentRegistration.html')


def studentProfile(request):
    user = User.objects.get(id= request.user.id)
    # if(User_Profile.objects.filter(user_id = user).exists):
    #     user_data = User_Profile.objects.get(user_id = request.user.id)    
    #     return render(request, 'studentPortal/studentProfile.html', {'user_data': user_data})
    # else:
    #     return render(request, 'studenPortal/studentProfile')   
    try:
        user_data = User_Profile.objects.get(user_id = request.user.id) 
        return render(request, 'studentPortal/studentProfile.html', {'user_data': user_data})
    except ObjectDoesNotExist:
        return render(request, 'studentPortal/studentProfile.html', {'message' : "Register to update your profile"})   


def studentAnalysis(request):
    user = User.objects.get(id= request.user.id)
    results = Analysis.objects.filter(user_id = user )
    for i in range(0, len(results)):
        results[i].detailed_result = json.loads(results[i].detailed_result)    
    return render(request, 'studentPortal/studentAnalysis.html', {'results_dict': results})
    
def gettingResult(request):
    user = User.objects.get(id= request.user.id)
    date =  datetime.date.today()
    points = request.POST['points']
    totalPoints = request.POST['totalPoints']
    skills_result = request.POST['skills_result']
    # print(skills_result)
    percentage = float(int(points)/int(totalPoints))*100
    if(percentage >= 80):
        status = "eligible"
    else:
        status = "suspended"
    data = Analysis(user_id = user, date = date, score = points, total = totalPoints, percentage = percentage, status = status, detailed_result = skills_result)
    data.save()
    print(data)
    print("data is saved")
    
    return render(request, 'studentPortal/studentDashboard.html')

def uploadResume(request):
    if(request.method == "GET"):
        return render(request, 'studentPortal/uploadResume.html')
    if(request.method == "POST"):
        user = User.objects.get(id= request.user.id)
        resume = request.FILES['resume']
        data = Resume(user_id = user, resume = resume)
        data.save()
        return render(request, 'studentPortal/studentDashboard.html')