from django.contrib import admin

from events.models import Event, Members, Schedule


class EventAdmin(admin.ModelAdmin):
    pass


class MembersAdmin(admin.ModelAdmin):
    pass


class ScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Schedule, ScheduleAdmin)
