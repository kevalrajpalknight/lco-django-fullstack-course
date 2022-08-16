from django.shortcuts import render
from .models import Youtuber


def youtubers_home(request):
    data = {
        'ytubers': Youtuber.objects.all(),
    }
    return render(request, 'youtubers/youtubers_home.html', data)

def youtubers_detail(request, id):
    YTuber = Youtuber.objects.get(id=id)
    data = {
        'YTuber':YTuber,
    }
    return render(request, 'youtubers/youtubers_single.html', data)

    


def search(request):
    YTubers = Youtuber.objects.all()
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            YTubers = YTubers.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            YTubers = YTubers.filter(city__exact=city)
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            YTubers = YTubers.filter(camera_type__exact=camera_type)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            YTubers = YTubers.filter(category__exact=category)

    data = {
        'YTubers':YTubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search,
    }
    return render(request, 'youtubers/search.html', data)
