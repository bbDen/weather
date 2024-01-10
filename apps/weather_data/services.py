from datetime import timezone

import requests

from apps.weather_data.models import Weather


def get_weather_from_openweathermap(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'.format(
        city=city, api_key='e03ba3dc926f8da352108b8898734ddc'
    )
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        weather_obj = Weather.objects.filter(city=city).first()

        if weather_obj:
            last_request_time = weather_obj.updated_at
            now = timezone.now()
            if (now - last_request_time).seconds < 30 * 60:
                weather_obj.temperature = temperature
                weather_obj.pressure = pressure
                weather_obj.wind_speed = wind_speed
                weather_obj.save()
                return {
                    'city': city,
                    'temperature': weather_obj.temperature,
                    'pressure': weather_obj.pressure,
                    'wind_speed': weather_obj.wind_speed,
                }

        try:
            weather = Weather.objects.create(
                city=city,
                temperature=temperature,
                pressure=pressure,
                wind_speed=wind_speed
            )
        except Exception as e:
            print(f"Ошибка при сохранении данных о погоде в базу данных: {e}")

        return {
            'city': city,
            'temperature': weather.temperature,
            'pressure': weather.pressure,
            'wind_speed': weather.wind_speed,
        }
    else:
        return {'error': 'Ошибка получения данных о погоде'}
