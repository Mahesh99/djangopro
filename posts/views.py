from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, CustomerMessageForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# request-response-cycle
posts = [
  {
    'title':'First post',
    'content':'First post content',
    'author':'Mahesh',
    'date':'30/04/2020'
  },
  {
    'title':'Second post',
    'content':'Second post content',
    'author':'Sai',
    'date':'30/04/2020'
  },

]

# address= {

# }


@login_required
def home(request):
  post_list = Post.objects.all().order_by('-create_date') 
  page = request.GET.get('page',1)

  paginator = Paginator(post_list,6)
  
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)

  context = {
    'posts':posts
  }

  return render(request,"posts/home.html",context)

def about(request):
  if request.method == 'POST':
    form = CustomerMessageForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,f'Message sent succesfully')
      return redirect('posts-about')
  else:
    form = CustomerMessageForm()
  return render(request,"posts/about.html",{'form':form})


def createPost(request):
  if request.method == "POST":
    form = CreatePostForm(request.POST)
    if form.is_valid():
      form.save(request.user)
      return redirect('posts-home')

  else:
    form = CreatePostForm()
  return render(request, 'posts/createpost.html', {'form':form})

def editPost(request, post_id):
  post = Post.objects.get(id=post_id) # get returns only 1 object if it exists otherwise error
  if request.method == 'POST':
    form = CreatePostForm(request.POST, instance=post)
    if form.is_valid():
      form.save(request.user)
      return redirect('posts-home')
  else:
    form = CreatePostForm(instance=post)

  return render(request,'posts/createpost.html',{'form':form})


def filters(request):
  nums = ['one','two','THREE','four']
  string = "hello\nworld\nhey"
  return render(request,'posts/filters.html',{'nums':nums,'string':string})












# Exercise 1
# TODO 1: create a contact_us() view
# TODO 2: set up path in the urls.py(posts app)
# TODO 3: access "http://localhost:8000/posts/contactus/"


# Exercise 2
# TODO 1: create a about_us string with some "lorem ipsum content" in this views.py below the posts list
# TODO 2: send this as a context to the about.html template
# TODO 3: inside it access the about_us string and dispaly it in a <p> tag inside <div> tag

# Exercise 3
# TODO : create contact details(email,phone,address) as dictionary and send it as a context to contactus.html template