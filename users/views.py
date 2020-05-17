from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm

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
  if request.method == 'POST':
    form_p = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    form_u = UserUpdateForm(request.POST, instance=request.user)
    if form_u.is_valid() and form_p.is_valid():
      form_u.save()
      form_p.save()
      messages.success(request,'Profile updated successfully')
      return redirect('profile')
  else:
    form_p = ProfileUpdateForm(instance=request.user.profile)
    form_u = UserUpdateForm(instance=request.user)
  context = {
    'form_u':form_u,
    'form_p':form_p,
  }
  return render(request,'users/profile.html',context)


# http codes
# 200,404,500,400,401,301