from django.shortcuts import render
from django.http import HttpResponse
from adminPortal.models import Question
from studentPortal.models import User_Profile
from json import dumps
from django.core import serializers
# importing uuid
import uuid

# Create your views here.

# test = 0


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
        # user = MyUUIDModel.objects.get(id=test)
        data = User_Profile(
            # user_id=user,
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
        # print(data)
        # print("data is saved")
    return render(request, 'studentPortal/studentRegistration.html')
