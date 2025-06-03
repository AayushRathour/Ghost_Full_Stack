from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'on'
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)  # Session expires when browser closes
                next_url = request.GET.get('next', '')
                if next_url and next_url.startswith('/'):  # Security check
                    return redirect(next_url)
                return redirect('index')
            else:
                messages.error(request, 'Your account is disabled.')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

@login_required(login_url='login')
def deepfake_demo(request):
    return render(request, 'deepfake-demo.html')

@login_required(login_url='login')
def fraud_demo(request):
    return render(request, 'fraud-demo.html')

@login_required(login_url='login')
def otp_demo(request):
    return render(request, 'otp-demo.html')

@login_required(login_url='login')
def voice_demo(request):
    return render(request, 'voice-demo.html')
