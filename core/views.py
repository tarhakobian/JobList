from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import RegistrationForm
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


# TODO// add validations
# @authenticate
@login_required(login_url='/login/')
def create_post(request):
    if request.method == "POST":
        post = Post()

        post.publisher_id = User.objects.get(username=request.session['username']).id
        post.category = request.POST['category']
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.requirements = request.POST['requirements']
        post.salary = request.POST['salary']
        post.contact_name = request.POST['contact_name']
        post.phone_number = request.POST['phone_number']
        post.email = request.POST['email']

        post.save()

        return redirect("home")

    return render(request, 'create_post.html')


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
