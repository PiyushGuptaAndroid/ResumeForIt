from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loggedInAsAdmin(request):
        return render(request, 'adminPortal/baseAdmin.html')

def addQuestions(request):
        print(request.method)
        if(request.method == "GET"):
                print("get method")
                return render(request, 'adminPortal/addQuestions.html')
        if(request.method == "POST"):
                print("post method")
                print(request.POST)     
                return render(request, 'adminPortal/addQuestions.html')   

def adminDashboard(request):
        return render(request, 'adminPortal/adminDashboard.html')

def eligibleCandidates(request):
        return render(request, 'adminPortal/eligibleCandidates.html')

def registerAdmins(request):
        return render(request, 'adminPortal/registerAdmins.html')

