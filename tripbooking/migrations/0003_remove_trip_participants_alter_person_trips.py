# Generated by Django 5.0 on 2024-01-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tripbooking', '0002_alter_person_trips_alter_trip_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='participants',
        ),
        migrations.AlterField(
            model_name='person',
            name='trips',
            field=models.ManyToManyField(to='tripbooking.trip'),
        ),
    ]
