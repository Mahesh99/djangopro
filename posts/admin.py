from django.contrib import admin
from .models import Post, CustomerMessage

# Register your models here.
admin.site.register(Post)
admin.site.register(CustomerMessage)