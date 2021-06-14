import datetime

from django.db import models
from django.db.models import Q


class ScheduleManager(models.Manager):
    def is_room_occupied(self, room_id: str, occupied_from: datetime.datetime, occupied_to: datetime.datetime) -> bool:
        queryset = self.get_queryset()
        queryset = queryset.filter(room_id=room_id)
        queryset = queryset.filter(
            Q(Q(occupied_from__lte=occupied_from) & Q(occupied_to__gte=occupied_from)) |
            Q(Q(occupied_from__lte=occupied_to) & Q(occupied_to__gte=occupied_to))
        )

        count = queryset.count()

        return count > 0
