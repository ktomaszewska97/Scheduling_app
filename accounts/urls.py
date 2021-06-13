from django.conf.urls import url
from .views import LoginView, RegisterView, profile_view

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^profile/$', profile_view),
]