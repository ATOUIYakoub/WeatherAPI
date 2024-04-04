""" Request handler module."""

from dotenv import load_dotenv
import os
import requests
import xmltodict
import json


load_dotenv()

def get_weather(city, country):
    """ Function to handle the requests to
        the 3rd API http://api.openweathermap.org ;
        Takes as arguments str "city" and "country", 
        and returns the formatted dictionary."
    """
    
    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&mode=xml"  # 3rd API"api.openweathermap.org" URL
    
    response = requests.get(url)                               # Response object
    
    
    data_json = json.dumps(xmltodict.parse(response.content))  # Converting the response to a json data
    current_data = json.loads(data_json)                       # Converting the json data to a Python Dictionary
    weather_data = current_data['current']                     # Extracting the relevant weather data
    
    
    # . . . . . . . .Weather variables Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

    location_name = "{}, {}".format(weather_data['city']['@name'], 
        weather_data['city']['country'])

    # Temperatures variables, given in °K  
    tempc = float(weather_data['temperature']['@value']) - 273.15  # Temperature in °C  ; Kelvin to Celsius formula:( °K − 273.15 = °C)
    tempf = (tempc * (9/5)) + 32                                   # Temperature from °K to °F
    

    """Wind variables, Sometimes there is low wind and the API returns None in the 
        values "speed" and "direction, so that´s why the conditionals implementation in the 
        wind values. """
    wind_speed = weather_data['wind']['speed']                              # Stores the value of wind speed             
    wind_descript_name = weather_data['wind']['speed']['@name'] if wind_speed != None else "No description available" # wind name ex: "Gentle breeze"
    wind_value = weather_data['wind']['speed']['@value'] if wind_speed != None else "No description available" # wind value in m/s
    wind_dir = weather_data['wind']['direction']                            # Stores the value of wind direction
    wind_direction = weather_data['wind']['direction']['@name'] if wind_dir != None else "No description available"       # Wind direction ex: "west-northwest"
    
    cloudiness = weather_data['clouds']['@name']                           # cloudiness name ex: "Scattered clouds"
    pressure = weather_data['pressure']['@value']                          # Pressure value in hpa
    humidity = weather_data['humidity']['@value']                          # Humidity value in %
    sunrise_list = weather_data['city']['sun']['@rise'].split("T")         
    sunrise = sunrise_list[1]                                              # Sunrise Hour
    sunset_list = weather_data['city']['sun']['@set'].split("T") 
    sunset = sunset_list[1]                                                # Sunset Hour
    
    # Geographical coordinates 
    coord_lat = weather_data['city']['coord']['@lat']                      # latitude value                 
    coord_lon = weather_data['city']['coord']['@lon']                      # longitude value                             
    
    requested_time = weather_data['lastupdate']['@value']                  
    

    # Final formatted data dictionary   
    weather_dict = {

        'location_name': location_name,
        'temperature': '%.2f°C, %.2f°F' % (tempc,tempf), 
        'wind': '{}, {} m/s, {}'.format(wind_descript_name, wind_value, wind_direction),                                    
        'cloudiness': cloudiness,                              
        'pressure': '{} hpa'.format(pressure),
        'humidity': '{} %'.format(humidity),
        'sunrise': sunrise, 
        'sunset': sunset,
        'geo_coordinates': '[{}, {}]'.format(coord_lat, coord_lon),
        'requested_time': requested_time,
        'forecast': '{...}'

    }

    return weather_dict                                                   # Send the dictionary to the view