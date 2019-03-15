from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts,})

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.all()