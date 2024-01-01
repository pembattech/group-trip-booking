# tripbooking/urls.py
from django.urls import path

from .views import trip_person

urlpatterns = [
    path('trip_person', trip_person, name='trip_person'),
]
