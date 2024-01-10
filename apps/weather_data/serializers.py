from rest_framework import serializers

from apps.weather_data.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('city', 'temperature', 'pressure', 'wind_speed', 'updated_at')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['temperature'] = instance.temperature
        return representation
