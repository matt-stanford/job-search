from django.db import models
from django.contrib.auth.models import User
import os

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='documents/', blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def filepath(self):
        return os.path.basename(self.resume.name)

    @property
    def filename(self):
        return f'{os.path.basename(self.resume.name)[:11]}...'

    def __str__(self):
        return self.user.username

    objects = models.Manager()
