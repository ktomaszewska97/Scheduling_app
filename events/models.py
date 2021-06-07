from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True) # added description
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_owner_id")  # Rename to owner

    def __str__(self):
        return self.name


class Members(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    role = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Rename to user
