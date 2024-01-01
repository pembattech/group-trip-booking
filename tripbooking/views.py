from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import HttpResponse

from .serializers import TripSerializer, PersonSerializer
from .models import Trip, Person


@api_view(["POST"])
def create_trip_person(request, format=None):
    data = request.data

    trip_name = data.get("trip").get("trip_name")
    existing_trip = Trip.objects.filter(trip_name=trip_name).first()

    if not existing_trip:
        trip_serializer = TripSerializer(data=data.get("trip"))
        if trip_serializer.is_valid():
            trip = trip_serializer.save()
        else:
            return Response({"error": trip_serializer.errors}, status=400)
    else:
        trip = existing_trip

    person_serializer = PersonSerializer(data=data.get("participants"))
    if person_serializer.is_valid():
        person = person_serializer.save(trips=[trip])
    else:
        trip.delete()
        return Response({"error": person_serializer.errors}, status=400)

    return Response({"trip_id": trip.id, "person_id": person.id})
