from django.urls import path

from .views import EventCreate, EventDetail

urlpatterns = [
    path('create/', EventCreate.as_view(), name='event-create'),
    path('detail/<uuid:pk>/', EventDetail.as_view(), name='event-detail'),
]