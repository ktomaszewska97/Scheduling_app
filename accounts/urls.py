from django.urls import path

from . import views

name_app = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.signup_view, name='register'),
]
