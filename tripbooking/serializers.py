from rest_framework import serializers

from .models import Trip, Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'mobile_no', 'location', 'landmark')

class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ("trip_name",)
