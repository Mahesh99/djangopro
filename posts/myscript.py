from .models import Post
from random import shuffle
from django.contrib.auth.models import User

def create_posts(n):
  users = list(User.objects.all())
  lor = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi repudiandae, accusantium, nulla error debitis quod quia distinctio vel ipsum esse facere et nobis fugiat, ut laboriosam. Explicabo recusandae est non!"
  for i in range(n):
    t = lor.split(" ")
    shuffle(t)
    shuffle(users)
    title = " ".join(t)[:6]
    content = " ".join(t)
    user = users[0]
    Post.objects.create(title=title,content=content,author=user).save()