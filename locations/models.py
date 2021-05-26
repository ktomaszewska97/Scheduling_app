from django.db import models


class Locations_Rooms(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField(null=True)
    locations_locations = models.ForeignKey('Locations_Locations', on_delete=models.CASCADE)


class Locations_Events(models.Model):
    occupied_from = models.DateTimeField(null=True)
    occupied_to = models.DateTimeField(null=True)
    status = models.CharField(max_length=45)
    locations_rooms = models.ForeignKey('Locations_Rooms', on_delete=models.CASCADE)


class Locations_Locations(models.Model):
    name = models.CharField(max_length=255)
    owner_id = models.ForeignKey('accounts.Account_Users', on_delete=models.CASCADE)
