from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TripSerializer, PersonSerializer
from .models import Trip, Person


@api_view(["POST", "GET"])
def trip_person(request, format=None):
    if request.method == 'POST':
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
    
    elif request.method == "GET":
        trips = Trip.objects.all()
        persons = Person.objects.all()

        trip_serializer = TripSerializer(trips, many=True)
        person_serializer = PersonSerializer(persons, many=True)

        response_data = {
            "trips": trip_serializer.data,
            "persons": person_serializer.data
        }

        return Response(response_data)

    return Response({"error": "Invalid request method"}, status=400)

@api_view(['GET'])
def get_person_of_trip(request, trip_name):
    persons_of_trip = Person.objects.filter(trips__trip_name__contains=trip_name)
    
    if persons_of_trip:

        person_serializer = PersonSerializer(persons_of_trip, many=True)
        response_data = {
                "trip_name": trip_name,
                "participants_of_trip": person_serializer.data,
            }

        return Response(response_data)
    return Response({"error": f"No participants found for trip '{trip_name}'"}, status=404)


    