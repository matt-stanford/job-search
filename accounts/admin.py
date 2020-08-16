from django.contrib import admin
from .models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'resume', 'date_uploaded', 'date_updated')

admin.site.register(Resume, ResumeAdmin)

