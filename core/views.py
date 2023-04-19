from django.http import Http404
from django.shortcuts import render
from .models import Post
from django.core.exceptions import ValidationError


def get_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_details(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except (Post.DoesNotExist, ValidationError):
        raise Http404("Post not found")
    return render(request, 'post.html', {'post': post})


