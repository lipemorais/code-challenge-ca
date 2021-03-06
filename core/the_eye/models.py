from django.db import models
import uuid


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_id = models.UUIDField()
    category = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    data = models.JSONField()
    timestamp = models.DateTimeField()
