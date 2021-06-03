from django.forms import ModelForm

from locations.models import Location, Room


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('owner_id', 'name')


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'size', 'status')