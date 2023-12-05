from django.db import models

# Create your models here.
class Flight (models.Model):
    flight_number =  models.IntegerField()
    flight_name = models.CharField(max_length =30)
    flight_time = models.FloatField()


