from rest_framework.response import Response
from rest_framework.views import APIView

from apps.weather_data.models import Weather
from apps.weather_data.services import get_weather_from_openweathermap


class WeatherAPIView(APIView):
    def get(self, request, city):
        weather = Weather.objects.filter(city=city).first()
        if weather:
            data = {
                'city': weather.city,
                'temperature': weather.temperature,
                'pressure': weather.pressure,
                'wind_speed': weather.wind_speed
            }
            return Response(data)
        else:
            weather_data = get_weather_from_openweathermap(city)
            return Response(weather_data)
