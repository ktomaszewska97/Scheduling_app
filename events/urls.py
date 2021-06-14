from django.urls import path

from .views import EventCreate, EventDetail, IndexView, ScheduleCreate

urlpatterns = [
    path('create/', EventCreate.as_view(), name='event-create'),
    path('detail/<uuid:pk>/', EventDetail.as_view(), name='event-detail'),
    path('', IndexView.as_view(), name='event-list'),
    path('detail/<uuid:pk>/schedule-crete/', ScheduleCreate.as_view(), name='schedule-crete'),
]