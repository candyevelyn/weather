import requests
from django.shortcuts import render
from bs4 import BeautifulSoup 
from . import models

BASE_URL='https://forecast.weather.gov/MapClick.php?lat=38.890370000000075&lon=-77.03195999999997#.XbDQK5NKjrI'

# Create your views here.
def home(request):
    return render(request, 'weather_app/base.html')

def extended(request):
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    final_forecast=[]

    for forecast in forecast_items:
        period = forecast.find(class_="period-name").get_text()
        short_desc = forecast.find(class_="short-desc").get_text()
        temp = forecast.find(class_="temp").get_text()
        img = forecast.find("img")
        src= 'https://forecast.weather.gov/'+ img['src']
        desc = img['title']

        final_forecast.append((period, short_desc, temp, src, desc ))

    forecast={
        'forecast': final_forecast
    }
    print(final_forecast)
    return render(request, 'weather_app/extended.html', forecast)