from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from locations.forms import LocationForm, RoomForm
from locations.models import Location, Room


class LocationsList(ListView):
    model = Location
    template_name = "locations/locations/list.html"
    paginate_by = 30


class LocationCreate(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "locations/locations/create.html"
    success_url = reverse_lazy("locations:location-list")


class LocationDetail(DetailView):
    model = Location
    template_name = "locations/locations/detail.html"


class RoomCreate(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'locations/rooms/create.html'

    def get_success_url(self):
        return reverse_lazy("locations:location-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.location_id = self.kwargs["pk"]

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
