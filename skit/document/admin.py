from django.contrib import admin
from .models import EmployeeDocument, MeetingDocument

# Register your models here.
admin.site.register(MeetingDocument)
admin.site.register(EmployeeDocument)
