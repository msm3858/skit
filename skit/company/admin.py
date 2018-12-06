from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Employee)
admin.site.register(Visitor)
admin.site.register(RoomReservation)
admin.site.register(Meeting)
admin.site.register(Room)
admin.site.register(MeetingParticipant)
