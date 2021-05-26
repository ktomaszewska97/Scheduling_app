from django.db import models


class Events_Members(models.Model):
    role = models.CharField(max_length=45)
    events_events_id = models.ForeignKey('Events_Events', on_delete=models.CASCADE)
    accounts_users_id = models.ForeignKey('accounts.Account_Users', on_delete=models.CASCADE)


class Events_Events(models.Model):
    name = models.CharField(max_length=45)
    owner_id = models.ForeignKey('accounts.Account_Users', on_delete=models.CASCADE)
    locations_rooms_id = models.ForeignKey('locations.Locations_Rooms', on_delete=models.CASCADE)
