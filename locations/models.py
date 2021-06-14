from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # rename owner_id => owner
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    size = models.IntegerField(null=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.location}: {self.name} ({self.size})"
