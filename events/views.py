from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from events.forms import EventForm
from events.models import Event


class EventCreate(CreateView):
    form_class = EventForm
    template_name = "events/create.html"

    def get_success_url(self):
        return reverse_lazy("events:event-detail", kwargs={"pk": self.object.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner_id = self.request.user

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class EventDetail(DetailView):
    model = Event
    template_name = "events/detail.html"
