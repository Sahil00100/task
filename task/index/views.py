from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

#signup
def signup(request):
    form=SignupForm
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.create_user()
            user.save()
    return render(request,'signup.html',{'form':form})
#login
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(
            request,
            username=email,
            password=password
            )

        if user is not None:
            auth_login(request,user)
            print(user)
            if user.is_superuser:
                #return render(request,'admin-dashboard.html',{})
                return redirect(reverse('admin:index'))
            else:
                user_details=User.objects.get(username=request.user)
                return render(request,'user-dashboard.html',{'user':user_details})

        else:
            messages.add_message(
                request,
                messages.INFO,
                'Invalid Username or password'
                )
    else:
        return render(request,'login.html',{})
    return render(request,'login.html',{})