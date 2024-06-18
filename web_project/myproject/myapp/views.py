from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Validate email format
        if not email.endswith('@email.com'):
            messages.error(request, 'Email must end with @email.com')
            return render(request, 'login.html')

        # Validate password complexity
        if len(password) < 8 or \
           not any(char.isdigit() for char in password) or \
           not any(char.isupper() for char in password) or \
           not any(char.islower() for char in password) or \
           not any(char in '!@#$%^&*()_+-=[]{};:\'",.<>/?' for char in password):
            messages.error(request, 'Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one symbol.')
            return render(request, 'login.html')

        # If everything is valid, you can proceed with further logic (e.g., authentication)

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return redirect('login')
