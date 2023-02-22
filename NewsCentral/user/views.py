from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    return render(request, 'user/home.html')


def signup(request):
    if request.method=='POST' and 'signup_submit' in request.POST:
        signup_username=request.POST.get('signup_username')
        signup_password1=request.POST.get('signup_password1')
        signup_password2=request.POST.get('signup_password2')

        if signup_password1!=signup_password2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(signup_username,None,signup_password1)
            my_user.save()
            print(my_user)
            return  render(request, 'user/useraccess.html')

    if request.method=='POST' and 'login_submit' in request.POST:
        login_username=request.POST.get('login_username')
        login_password=request.POST.get('login_password')

        user=authenticate(request,username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            return redirect('')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return redirect('/')
