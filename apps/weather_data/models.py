from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=255)
    pressure = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
    wind_speed = models.FloatField()
    temperature = models.FloatField()
