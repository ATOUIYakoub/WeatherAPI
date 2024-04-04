from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from .serializers import WeatherSerializer

# Utilities
import json
from . requestapi import get_weather

# Cache
from django.core.cache import cache




@api_view(['GET'])
def weather_detail(request):                                
    """Receive the client request and return a JSON 
        response with the given city and country."""
    
    serializer = WeatherSerializer(data=request.GET)           # Pass the request data to the serializer WeatherSerializer() model  
    serializer.is_valid()                                      # return True if serializer fields are valid

    # Retrieve the validated data from serializer
    country = serializer.validated_data['country']
    city = serializer.validated_data['city']     
    
    weather_data = get_weather(city, country)                   # Call to get_weather function who returns a formatted dictionary

    #  Using Low-level cache API
    if cache_data := cache.get("{}-{}".format(country, city)):  # look if the key is already in the cahe table
        return Response(weather_data)                           # Return the stored object 
    
    cache.set("{}-{}".format(country, city), weather_data, timeout=60*2)  # Storing the object in the cahe table with a Timeout of 2 Minutes
    

    return Response(weather_data)

        
    