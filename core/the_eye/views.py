from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from the_eye.models import Event
from the_eye.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoints to CRUD Event
    """
    queryset = Event.objects.all().order_by('-timestamp')
    serializer_class = EventSerializer
