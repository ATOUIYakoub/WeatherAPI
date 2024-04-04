from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Serializers
from .serializers import WeatherSerializer

# Utilities
import json
from . requestapi import get_weather

# Cache
from django.core.cache import cache




@api_view(['GET'])
def weather_detail(request):
    """Receive the client request and return a JSON response with the given city and country."""
    
    serializer = WeatherSerializer(data=request.query_params)  # Use request.query_params instead of request.GET
    serializer.is_valid()

    # Retrieve the validated data from serializer
    country = serializer.validated_data.get('country')  # Use get() method to avoid KeyError
    city = serializer.validated_data.get('city')

    if not country or not city:
        return Response({"error": "Both 'country' and 'city' parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

    weather_data = get_weather(city, country)

    # Using Low-level cache API
    cache_key = "{}-{}".format(country, city)
    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    cache.set(cache_key, weather_data, timeout=60*2)

    return Response(weather_data)
 