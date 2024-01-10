from django.contrib import admin
from django.urls import path

from apps.weather_data.views import WeatherAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/<city>/', WeatherAPIView.as_view(), name='weather-by-city'),
]
