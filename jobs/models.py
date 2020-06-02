from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobId = models.CharField(max_length=255, null=True)
    jobTitle = models.CharField(max_length=255)
    locationName = models.CharField(max_length=255)
    employerName = models.CharField(max_length=255)
    jobUrl = models.URLField()
    saveDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.jobTitle

    objects = models.Manager()

