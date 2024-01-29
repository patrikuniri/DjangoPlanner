from django.db import models
from event_management.models import Event

class Participant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    # Add the email field with a default value
    email = models.EmailField(default='example@example.com')
    accepted = models.BooleanField(default=False)
    event = models.CharField(max_length=100, default='Default Event')
