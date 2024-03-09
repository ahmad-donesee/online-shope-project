from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
from .forms import UserForm


def register_home(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.save()
            login(request,user)
            return redirect("product:product_view")
    else:
        return render(request,"register/register.html",{"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if  form.is_valid():
            user_name=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=user_name,password=password)
            if user  is not None :
                user.save()
                login(request,user)
                messages.info(request, f"You are now logged in as {user_name}.")
                return redirect('product:product_view')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form=AuthenticationForm()
    return render(request,'register/login.html',{'form':form}) 
    

def logout_view(request):
    logout(request)
    return redirect("product:product_view")