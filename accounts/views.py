from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, FormView, DetailView
from events.models import Event, Schedule
from accounts.forms import TeamCreateForm
from accounts.models import Team, TeamMember


class LoginView(DjangoLoginView):
    template_name = "accounts/login.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")


class TeamCreateView(FormView):
    form_class = TeamCreateForm
    template_name = "accounts/create.html"
    success_url = ""

    def form_valid(self, form):
        with transaction.atomic():
            team = Team(name=form.cleaned_data["name"])
            team.owner = self.request.user
            team.save()

            team_members_list = []
            for member in form.cleaned_data["members"]:
                team_members_list.append(TeamMember(team=team, user=member))

            TeamMember.objects.bulk_create(team_members_list)

        return super(TeamCreateView, self).form_valid(form)


class TeamUpdateView(FormView):
    form_class = TeamCreateForm
    template_name = "accounts/update.html"
    success_url = ""

    def get_form_kwargs(self):
        kwargs = super(TeamUpdateView, self).get_form_kwargs()

        team = Team.objects.get(id=self.kwargs["id"])

        initial = {
            "name": team.name,
            "members": TeamMember.objects.filter(team=team).values_list('user_id', flat=True),
        }

        kwargs["initial"] = initial

        return kwargs

    def form_valid(self, form):
        with transaction.atomic():
            team = Team.objects.get(id=self.kwargs["id"])
            team.name = form.cleaned_data["name"]
            team.owner = self.request.user
            team.save()

            TeamMember.objects.filter(team=team).delete()

            team_members_list = []
            for member in form.cleaned_data["members"]:
                team_members_list.append(TeamMember(team=team, user=member))

            TeamMember.objects.bulk_create(team_members_list)

        return super(TeamUpdateView, self).form_valid(form)


def profile_view(request):
    user = request.user
    event = Schedule.objects.select_related('event').filter(event__owner_id=user.id)

    context = {
        'user': user,
        'events': event,
        #'schedule': schedule,
    }
    template = 'accounts/profile.html'
    return render(request, template, context)
