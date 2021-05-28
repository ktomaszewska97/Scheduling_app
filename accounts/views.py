from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Registration successful.")
        return redirect("main:homepage")
    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm
    return render(request, 'templates/accounts/register.html', {'signup_form': form})
