from ast import Return
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
        fname=request.POST['fname']
        lname=request.POST['lname']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'username already exits')
            return redirect("/signup")
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exits')
            return redirect("/signup")
        elif password!=rpassword:
            messages.error(request,'passwords missmatch')
            return redirect("/signup")
        else:
            user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            return redirect("/")
            messages.success(request,"sucessfully signed up")      
    else:
        return render(request,'signup.html')
def ulogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if not User.objects.filter(email=email).exists():
            messages.warning(request,'invalid email id')
            return redirect('/')
        data=User.objects.filter(email=email).get()
        user=auth.authenticate(username=data.username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.warning(request,'Invalid email and password')
            return redirect('/ulogin')
    else:
        return render(request,'ulogin.html')
def logout(request):
    auth.logout(request)
    messages.warning(request,'sucessfully logout')
    return redirect('/')
