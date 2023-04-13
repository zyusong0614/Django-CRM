from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    # Click to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In Successfully:)')
            return redirect('home')
        else:
            messages.success(request, 'There Was A Problem During Logging In!')
            return redirect('home')

    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})
