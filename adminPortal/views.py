from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loggedInAsAdmin(request):
        return render(request, 'adminPortal/baseAdmin.html')

