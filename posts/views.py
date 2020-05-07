from django.shortcuts import render, HttpResponse
from .models import Post
from django.contrib.auth.models import User

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


def home(request):
  # user = User.objects.filter(username="mahesh").first()
  # posts = Post.objects.filter(author=user)

  posts = Post.objects.filter(author__username="mahesh")

  context = {
    'posts':posts
  }

  return render(request,"posts/home.html",context)

def about(request):
  return render(request,"posts/about.html")



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