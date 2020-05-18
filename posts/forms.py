from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title','content']
  
  def save(self, author):
    self.instance.author = author
    super().save()