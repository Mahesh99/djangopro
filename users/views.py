from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
  if request.method == "POST":
    form = UserRegistrationForm(request.POST) # bound form
    if form.is_valid():
      form.save() # a new user is created in User model or table
      messages.success(request,'Account has been created successfully')
      return redirect('posts-home')
  else:
    form = UserRegistrationForm() # unbound form
  
  return render(request,'users/register.html',{'form':form})

def profile(request):
  return render(request,'users/profile.html')


# http codes
# 200,404,500,400,401,301