from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .classes import RegistrationForm
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_details(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except (Post.DoesNotExist, ValidationError):
        raise Http404("Post not found")
    return render(request, 'post.html', {'post': post})


def profile(request):
    return render(request, 'profile.html')


@csrf_protect
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            request.session['username'] = username

            return redirect('home')
        else:
            context = {'error_message': 'Invalid username or password'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


@csrf_protect
def register_page(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)
