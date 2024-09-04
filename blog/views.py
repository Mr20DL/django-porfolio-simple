from django.shortcuts import render
from .models import Post

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    return render(request, 'post_detail.html', {"post": post_id})