from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        if p1 == p2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exist...')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist..')
                return redirect('register')
            else:
                s=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=p1)
                s.save()
        else:
            messages.info(request,'password not matched..')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        p1=request.POST['password1']
        s=auth.authenticate(username=uname,password=p1)
        if s is not None:
            auth.login(request,s)
            return redirect('/')
        else:
            messages.info(request,'user not exist..')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')