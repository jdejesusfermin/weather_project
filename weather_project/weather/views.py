import requests
from django.shortcuts import render

def index(request):
    api_key = 'dedd28eeab69a075a8a070e878364965'
    city = 'Manila'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    weather_data = response.json()

    context = {
        'city': city,
        'weather': weather_data
    }

    return render(request, 'weather/index.html', context)