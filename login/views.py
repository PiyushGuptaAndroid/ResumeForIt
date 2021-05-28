from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import  CreateUserForm



def registerPage(request):
	# if request.user.is_authenticated:
	# 	return render(request, 'studentPortal/studentDashboard.html')
	# else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'login/register.html', context)

def loginPage(request):
	if (request.user.is_authenticated and request.user.username != 'admin'):
		return HttpResponseRedirect('/adminDashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/studentDashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def adlogoutUser(request):
	logout(request)
	return redirect('alogin')

# @login_required(login_url='login')
# def home(request):
# 	return render(request, 'studentPortal/studentDashboard.html')

def open(request):
	return render(request, 'login/open.html')

def adminLogin(request):
	if request.method == 'POST':
		username=request.POST["username"]
		password=request.POST["password"]
		if Recruiter.objects.filter(username=username,password=password).exists():
			obj=Recruiter.objects.filter(username=username,password=password)
			# print(obj)
			request.session['user']=username
			# request.session['email']=obj["email"]
			return HttpResponseRedirect('/adminDashboard')
		else:
			messages.info(request, 'Invalid Crendtial.')
	return render(request, 'login/alogin.html', {})

