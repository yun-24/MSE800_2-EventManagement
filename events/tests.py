from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

from events.models import Event


class EventTests(TestCase):
    def setUp(self):
        self.regular_user = User.objects.create_user(username='testuser', password='testpass')

        self.event = Event.objects.create(
            title='Test Event',
            description='<p>This is a test event.</p>',
            date_time=timezone.now() + timedelta(days=1),
            location='Test Location',
            organizer=self.regular_user
        )

    def test_create_event(self):
        # Log in
        self.client.login(username='testuser', password='testpass')

        url = reverse('events:create_event')
        data = {
            'title': 'New Event',
            'description': '<p>New event with CKEditor content</p>',
            'date_time': (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%dT%H:%M'),
            'location': 'New Location'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Should redirect on success
        new_event = Event.objects.get(title='New Event')
        self.assertEqual(new_event.location, 'New Location')
        self.assertEqual(new_event.organizer, self.regular_user)

    def test_event_attendance(self):
        # Log in
        self.client.login(username='testuser', password='testpass')
        url = reverse('events:event_detail', kwargs={'pk': self.event.pk})
        # Simulate the attend action as a POST request with a field 'action' set to 'attend'
        response = self.client.post(url, {'action': 'attend'})
        # Expect a redirect after processing
        self.assertRedirects(response, url)
        self.event.refresh_from_db()
        self.assertIn(self.regular_user, self.event.attendees.all())