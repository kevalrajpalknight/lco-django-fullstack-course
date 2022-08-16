from django.shortcuts import render, redirect
from .models import Hiretuber
from django.contrib import messages

# Create your views here.
def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        tuber_id = request.POST.get('tuber_id')
        tuber_name = request.POST.get('tuber_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        user_id = request.POST.get('user_id')
        message = request.POST.get('message')

        hiretuber = Hiretuber(
            first_name = first_name,
            last_name = last_name,
            email = email,
            tuber_id = tuber_id,
            tuber_name = tuber_name,
            city = city,
            state = state,
            phone = phone,
            user_id = user_id,
            message = message,
        )
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
    return redirect('hiretubers:home')