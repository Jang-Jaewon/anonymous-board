from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from user.models import User


def signin(request):
    if request.method == 'GET':
        return render(request, 'page/signin.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('board')
        else:
            messages.error(request, "입력 값을 확인해주세요.")
            return redirect('signin')
        
    
def signup(request):
    if request.method == 'GET':
        return render(request, 'page/signup.html')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 아이디입니다')
            return redirect('signup')
        else:
            user = User(
                username=username,
                password=make_password(password),
                nickname=nickname,
            )
            user.save()
            login(request, user)
            return redirect('board')


def signout(request):
    if request.method == "GET":
        logout(request)
        return redirect('board')
