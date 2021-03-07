import uuid

from django.test import TransactionTestCase

from the_eye.models import Event


class ModelTestCase(TransactionTestCase):
    """This class defines the test suite for the Event model."""

    def test_model_can_create_an_event(self):
        """Test the event model can create a bucketlist."""
        # Arrange
        self.event = Event(
            session_id=uuid.uuid4(),
            category="page interaction",
            name="pageview",
            data={"host": "www.consumeraffairs.com", "path": "/"},
            timestamp="2021-01-01 09:15:27.243860",
        )

        old_count = Event.objects.count()

        # Act
        self.event.save()
        new_count = Event.objects.count()

        # Assert
        self.assertEqual(old_count + 1, new_count)
