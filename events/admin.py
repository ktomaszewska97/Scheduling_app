from django.contrib import admin
from events.models import Event, Members


class EventAdmin(admin.ModelAdmin):
    pass


class MembersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Members, MembersAdmin)
