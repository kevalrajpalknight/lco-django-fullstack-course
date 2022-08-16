from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'Successfully Login!')
            return redirect('accounts:dashboard')

        else:
            messages.error(request, 'Invalid Credentials.')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Successfull!')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email_address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email address already exists')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(
                        username=username, 
                        email=email, 
                        password=password, 
                        first_name=firstname,
                        last_name=lastname,
                    )
                    user.save()
                    messages.success(request, "Account Created Successfully!")
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('accounts:register')
    data = {}
    return render(request, 'accounts/register.html', data)

@login_required(login_url='accounts:login')
def dashboard(request):
    data = {}
    return render(request, 'accounts/dashboard.html', data)