from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.template import RequestContext
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import  csrf_exempt

from .forms import UsersInfo,RegisterForm

def login_view(request):
    form = UsersInfo(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        if next:
            return redirect(next)

        return redirect('/')

    return render(request,'users/login.html',{'form':form})

@csrf_exempt
def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login_user = authenticate(username=user.username, password=password)
        login(request,login_user)
        return redirect('/')


    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)

    # return render(request,'cars/home.html',{})
    return redirect('/')


