from django.conf.urls import url
from django.urls import path

from .views import LoginView, RegisterView, profile_view, TeamCreateView, TeamUpdateView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    path(r'profile/', profile_view, name='profile-view'),
    path(r'team/crete/', TeamCreateView.as_view(), name='team-create'),
    path(r'team/<uuid:id>/update/', TeamUpdateView.as_view(), name='team-update'),
]