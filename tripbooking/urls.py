# tripbooking/urls.py
from django.urls import path

from .views import trip_person, get_person_of_trip

urlpatterns = [
    path('trip_person', trip_person, name='trip_person'),
    path('get_person_of_trip/<str:trip_name>', get_person_of_trip, name='get_person_of_trip'),
]
