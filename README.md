# Weather Information App

This is a simple Django web application that fetches and displays weather information for a given city using the OpenWeatherMap API.

## Features

- Displays current weather data (temperature, description, and icon) for a user-provided city.
- Handles errors for unknown cities or network issues.
- Displays the current date along with weather details.

##Screenshots
![image](https://github.com/user-attachments/assets/02c7e339-bd0a-4f50-9730-ed9ac38ee786)


## Requirements

- Python 3.x
- Django 3.x or higher
- Requests library
- An OpenWeatherMap API key (free tier available)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/weather-info-app.git

Process:
cd weather-info-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
Open http://127.0.0.1:8000/ in your browser to use the app.

***Usage***
Enter a city name in the input field and click "Get Weather" to retrieve the current weather.
The application will display:
The weather description (e.g., "clear sky")
The temperature in Celsius
An icon representing the weather
The current date

***Error Handling***
If the city is not found, an error message will be displayed.
If there is a network issue, an error message will be shown.

***Connect with me ***
LinkedIn: https://www.linkedin.com/in/techbyabrar/
