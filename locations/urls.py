from django.urls import path

from .views import LocationCreate, LocationsList, LocationDetail, RoomCreate

urlpatterns = [
    path('create/', LocationCreate.as_view(), name='location-create'),
    path('list/', LocationsList.as_view(), name='location-list'),
    path('detail/<uuid:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('detail/<uuid:pk>/room-create/', RoomCreate.as_view(), name='room-create'),

]
