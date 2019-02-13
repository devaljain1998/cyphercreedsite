from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    title = "Admin's Blog"
    return render(request,'blog/post_list.html',{'posts':posts,'title':title})