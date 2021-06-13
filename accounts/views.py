from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from events.models import Event


class LoginView(DjangoLoginView):
    template_name = "accounts/login.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")


def profile_view(request):
    user = request.user
    event = Event.objects.all().filter(owner_id=user.id)
    context = {
        'user': user,
        'events': event,
    }
    template = 'accounts/profile.html'
    return render(request, template, context)
