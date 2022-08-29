from weatherapp.models import City
from django.shortcuts import get_object_or_404, redirect, render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages

def home(request):
    API_KEY = config('API_KEY')
    city = 'Viyana'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    content = response.json()

    context = {
        'city': content['main']['temp'],
        'temp': content['name'],
        'desc': content['weather'][0]['description'],
        'icon': content['weather'][0]['icon'],
    }


    return render(request, 'weatherapp/home.html')

