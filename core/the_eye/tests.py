import uuid

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITransactionTestCase
from django.test import TransactionTestCase

from .models import Event


class EventTests(APITransactionTestCase):
    """Test suite for API Testing"""

    def test_create_event(self):
        """
        Ensure we can create a new Event object.
        """
        # Arrange
        url = reverse('event-list')
        body = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860"
        }
        # Act
        response = self.client.post(url, body, format='json')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().session_id, uuid.UUID('e2085be5-9137-4e4e-80b5-f1ffddc25423'))


class ModelTestCase(TransactionTestCase):
    """This class defines the test suite for the Event model."""

    def test_model_can_create_an_event(self):
        """Test the event model can create a bucketlist."""
        # Arrange
        self.event = Event(session_id=uuid.uuid4(),
                           category="page interaction",
                           name="pageview",
                           data={
                               "host": "www.consumeraffairs.com",
                               "path": "/"
                           },
                           timestamp="2021-01-01 09:15:27.243860")

        old_count = Event.objects.count()

        # Act
        self.event.save()
        new_count = Event.objects.count()

        # Assert
        self.assertEqual(old_count + 1, new_count)
