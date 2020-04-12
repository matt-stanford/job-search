from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('user', 'jobTitle', 'locationName', 'employerName', 'saveDate')

admin.site.register(Job, JobAdmin)
