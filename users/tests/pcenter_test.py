from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from events.models import Event
from users.views import personal_center
from django.urls import reverse

class PersonalCenterViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.event1 = Event.objects.create(name='Event 1', organizer=self.user)
        self.event2 = Event.objects.create(name='Event 2', attendees=[self.user])

    def test_personal_center_UserAuthenticated_ShouldRenderTemplate(self):
        request = self.factory.get('/personal_center/')
        request.user = self.user
        response = personal_center(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/personal_center.html')
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Event 1')
        self.assertContains(response, 'Event 2')

    def test_personal_center_UserNotAuthenticated_ShouldRedirectToEventList(self):
        request = self.factory.get('/personal_center/')
        request.user = User()  # 未认证用户
        response = personal_center(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('events:event_list'))
