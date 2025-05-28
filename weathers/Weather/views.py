from django.shortcuts import render, HttpResponse
import json
import urllib.request
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        
        if not city:
            messages.error(request, 'Please enter a city name')
            return render(request, 'index.html', {'data': {}})
            
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=610b1096ece1cbcac6a7339236988b18').read()
            json_data = json.loads(res)
            data = {
                "city": city,
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon'])+'° ' + str(json_data['coord']['lat'])+'°',
                "temp": str(round(float(json_data['main']['temp']) - 273.15, 2))+'°C',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except urllib.error.HTTPError as e:
            messages.error(request, f'City not found. Please enter a valid city name.')
            data = {}
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.')
            data = {}
    else:
        data = {}
        
    return render(request, 'index.html', {'data': data})
