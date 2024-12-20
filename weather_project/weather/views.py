import requests
from django.shortcuts import render
from django.conf import settings


def get_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def home(request):
    city = request.GET.get('city', 'London')  # Default to London if no city is provided
    weather_data = get_weather_data(city)
    context = {
        'city': city,
        'weather': weather_data
    }
    return render(request, 'weather/home.html', context)
# Create your views here.
