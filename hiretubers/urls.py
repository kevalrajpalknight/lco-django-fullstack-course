from django.urls import path
from . import views
app_name = 'hiretubers'

urlpatterns = [
    path('', views.hiretuber, name="home")
]