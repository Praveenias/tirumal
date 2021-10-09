from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import register
# Create your views here.

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'index.html')

def form(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['password']
    trueData = register.objects.filter(username=a,password=b)
    if trueData:
        return redirect(home)
    return redirect(login)

def registerr(request):
    return render(request,'register.html')

def registerdata(request):
    if request.method == 'POST':
        name = request.POST['userName']
        passw = request.POST['password']
        email = request.POST['emailAddress']
        number = request.POST['phoneNumber']
    data = register(username=name,password=passw,email=email,number=number)
    data.save()
    return redirect(login)