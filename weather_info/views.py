from django.shortcuts import render
import requests
import datetime

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'Moscow')
    else:
        city = request.GET.get('city', 'Moscow')  # Use GET method for form

    api_key = '4be5caf3ed173b94bae5d06bee914848'  # Ensure this is correct
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(url, params=params)  
        data = response.json()  

        if response.status_code == 200:
            context = {
                'description': data.get('weather', [{}])[0].get('description', 'No description'),
                'icon': data.get('weather', [{}])[0].get('icon', '01d'),
                'temp': data.get('main', {}).get('temp', 'N/A'),
                'date': datetime.date.today(),
                'city': city
            }
        else:
            context = {'error': 'City not found. Try again!', 'date': datetime.date.today(), 'city': city}

    except requests.exceptions.RequestException:
        context = {'error': 'Network error. Please check your connection!', 'date': datetime.date.today(), 'city': city}

    return render(request, 'weather_info/index.html', context)
