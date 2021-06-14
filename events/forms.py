from django.forms import ModelForm

from events.models import Event


from django import forms
from django.forms import ModelForm

from events.models import Event, Schedule


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name",)


class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ("room", "occupied_from", "occupied_to")
        widgets = {
            "occupied_from": DateTimeInput(),
            "occupied_to": DateTimeInput(),
        }

    def clean(self):
        cleaned_data = super(ScheduleForm, self).clean()
        room_id = cleaned_data.get("room")
        occupied_from = cleaned_data.get("occupied_from")
        occupied_to = cleaned_data.get("occupied_to")

        if occupied_to < occupied_from:
            self.add_error("occupied_to", "The end date of the reservation must be greater than the start date")
            return cleaned_data

        is_room_occupied = Schedule.objects.is_room_occupied(room_id, occupied_from, occupied_to)
        if is_room_occupied:
            self.add_error("occupied_from", "The room is already reserved during the selected hours")

        return cleaned_data
