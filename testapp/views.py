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
        return render(request,'index.html',{'username':a})
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
def forget(request):
    data = "welcome to forget password"
    return render(request,'forgetpass.html',{'data1':data})

def changepass(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
    register.objects.filter(username=username).update(password=pass1)
    return redirect(login)

def displayuser(request):
    userData = register.objects.all()
    return render(request,'displayuser.html',{'userData':userData})