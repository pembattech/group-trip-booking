# tripbooking/urls.py
from django.urls import path

from .views import create_trip_person

urlpatterns = [
    path('create_trip_person', create_trip_person, name='create_trip_person'),
]
