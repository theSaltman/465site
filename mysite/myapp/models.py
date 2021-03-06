from django.db import models
from django.utils import timezone

# Create your models here.
class Suggestion(models.Model):
    suggestion_field = models.CharField(max_length=240)

    def __str__(self):
        return str(self.suggestion_field)

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
#    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
