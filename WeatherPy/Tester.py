# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
from scipy.stats import linregress
import json

# Impor the OpenWeatherMap API key
from api_keys import weather_api_key

# Import citipy to determine the cities based on latitude and longitude
from citipy import citipy
# Empty list for holding the latitude and longitude combinations
lat_lngs = []

# Empty list for holding the cities names
cities = []

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(f"Number of cities in the list: {len(cities)}")
#Mircea
cities_df = pd.DataFrame({'City':cities})
print(cities_df.head())
#url = "api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=228503c9f17c09eda6fdb8f687f928e6"
url = 'http://api.openweathermap.org/data/2.5/weather?q=bucharest&APPID=fd80fb29f3b6c7f602f82a7557aeff9d'
city_url = f"{url}&{city}&appid={weather_api_key}"
# Make the API request
response = requests.get(url)
response_json = response.json()
temperatu = response_json['main']['temp']
print("temperature is: ",temperatu)
print(response_json)

city_weather = requests.get(city_url)    # YOUR CODE HERE
city_weather_json = city_weather.json()
   # Parse out latitude, longitude, max temp, humidity, cloudiness, wind speed, country, and date
city_lat = city_weather_json['coord']['lat']# YOUR CODE HERE
city_lng = city_weather_json['coord']['lon']# YOUR CODE HERE
city_max_temp = city_weather_json['main']['temp_max']# YOUR CODE HERE
city_humidity = city_weather_json['main']['humidity']# YOUR CODE HERE
city_clouds = city_weather_json['clouds']['all']# YOUR CODE HERE
city_wind = city_weather_json['wind']# YOUR CODE HERE
print('Info on ',city,': ',city_lat,' ',city_humidity,' ',city_clouds,' ',city_wind)