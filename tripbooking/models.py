from django.db import models

class Trip(models.Model):
    trip_name = models.CharField(max_length=255)

class Person(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    trips = models.ManyToManyField('Trip')
    
    def __str__(self):
        return self.name
