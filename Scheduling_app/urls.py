from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("locations/", include(("locations.urls", "locations"), namespace="locations")),
    path("events/", include(("events.urls", "events"), namespace="events")),
]