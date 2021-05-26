from django.contrib import admin
from .models import Locations_Rooms, Locations_Events, Locations_Locations

admin.site.register(Locations_Rooms)
admin.site.register(Locations_Events)
admin.site.register(Locations_Locations)
