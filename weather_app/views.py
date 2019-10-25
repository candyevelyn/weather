import requests
from django.shortcuts import render
from bs4 import BeautifulSoup 
from . import models

BASE_URL='https://forecast.weather.gov/MapClick.php?lat=38.890370000000075&lon=-77.03195999999997#.XbDQK5NKjrI'
RADAR_URL ='https://radar.weather.gov/ridge/radar_lite.php?rid=LWX&product=N0R&loop=yes'


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


def current(request):
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    current=soup.find(id="current_conditions-summary")
    src='https://forecast.weather.gov/'+current.find("img")['src']
    conditions=current.find(class_="myforecast-current").get_text()
    temp_f= current.find(class_="myforecast-current-lrg").get_text()
    temp_c=current.find(class_="myforecast-current-sm").get_text()
    table=soup.find(id="current_conditions_detail")
    col=table.find_all('tr')
    conditions_detail=[]

    for row in col:
        detail=row.find(class_="text-right")
        conditions_detail.append(detail.next_sibling.next_sibling.get_text())

    current_summary={
        'src': src,
        'conditions': conditions,
        'temp_f':temp_f,
        'temp_c':temp_c,
        'humidity':conditions_detail[0],
        'wind_speed':conditions_detail[1],
        'barometer':conditions_detail[2],
        'dewpoint':conditions_detail[3],
        'visibility':conditions_detail[4],
        'last_update':conditions_detail[5],
    }
    return render(request, 'weather_app/current.html', current_summary)

def radar(request):
    page = requests.get(RADAR_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    image=soup.find(id="image0")
    radar_image=image.find('img')
    src='https://radar.weather.gov/'+radar_image['src']
    print(src)
    radar={
        'src':src,
    }

    return render(request, 'weather_app/radar.html', radar)

def discussion(request):
    page = requests.get('https://forecast.weather.gov/product.php?site=LWX&issuedby=LWX&product=AFD&format=CI&version=1&glossary=1&highlight=off')
    soup = BeautifulSoup(page.content, 'html.parser')
    content= soup.find(id='proddiff')
    content.span.decompose()
    discussion=content.get_text()
 


    text={
        'text':discussion,
    }

    return render(request, 'weather_app/discussion.html', text)
