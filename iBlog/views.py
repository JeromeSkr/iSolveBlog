from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import IBlogModel
from django.contrib.auth.hashers import make_password


def homepage(request):
    posts = IBlogModel.objects.all()
    return render(request, 'homepage.html', {'posts':posts})


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        uemail = request.POST.get('email')
        pwd = request.POST.get('password')
        pwd1 = request.POST.get('password1')
        if pwd == pwd1:
            obj = User(username=uname, email= uemail, password=make_password(pwd1))
            obj.save()
            return redirect('login_page')
        else:
            messages.error(request, "Enter valid details!")
            return render (request, 'register.html')
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        access = authenticate(username=uname, password=pwd)
        if access:
            login(request, access)
            return redirect('homepage')
        else:
            messages.error(request, "Enter valid details!")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('homepage')

@login_required(login_url='login_page')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        IBlogModel.objects.create(title=title, content=content,author=request.user)
        return redirect('homepage')

    return render(request, 'create.html')

@login_required(login_url='login_page')
def edit_post(request, post_id):
    post = get_object_or_404(IBlogModel, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('homepage')
    return render(request, 'edit.html', {'post':post})

@login_required(login_url='login_page')
def delete_post(request, post_id):
    post = get_object_or_404(IBlogModel, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('homepage')
    return render(request, 'delete.html', {'post':post})

def details(request, post_id):
    post = get_object_or_404(IBlogModel, id=post_id)
    return render(request, 'details.html', {'post':post})