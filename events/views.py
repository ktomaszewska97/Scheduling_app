from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
import datetime

from events.forms import EventForm, ScheduleForm
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


class ScheduleCreate(CreateView):
    form_class = ScheduleForm
    template_name = "events/create.html"

    def get_success_url(self):
        return reverse_lazy("events:event-detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.event_id = self.kwargs["pk"]

        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class IndexView(ListView):
    #model = Event
    context_object_name = 'event-list'
    template_name = "events/list.html"
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['date'] = datetime.datetime.now()
        # the rest of the models
        return context
