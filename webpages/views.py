from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber

def home(request):
    slider = Slider.objects.all()[:3]
    teams = Team.objects.all()
    ytubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_ytubers = Youtuber.objects.order_by('-created_date')
    data = {
        'slider': slider,
        'team': teams,
        'featured_ytubers': ytubers,
        'YTubers': all_ytubers,
    }
    return render(request, 'webpages/home.html', context=data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')

def about(request):
    return render(request, 'webpages/about.html')