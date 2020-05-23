from django import forms
from .models import Post, CustomerMessage


class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','content']
  
  def save(self, author):
    self.instance.author = author
    super().save()

class CustomerMessageForm(forms.ModelForm):
  class Meta:
    model = CustomerMessage
    fields = ['name','email','subject','message']
