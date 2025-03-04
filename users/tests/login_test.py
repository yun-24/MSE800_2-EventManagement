from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class UserLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = self.create_user(username='testuser', password='testpassword')

    def create_user(self, username, password):
        from django.contrib.auth.models import User
        return User.objects.create_user(username=username, password=password)

    @patch('users.views.login')
    def test_user_login_ValidCredentials_UserLoggedinAndRedirected(self, mock_login):
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'testpassword'})
        # make sure login function is called
        self.assertTrue(mock_login.called)
        mock_login.assert_called_once_with(response.wsgi_request, self.user)
        # make sure user is redirected, status code is 302
        self.assertEqual(response.status_code, 302)

    def test_user_login_InvalidCredentials_FormErrorsDisplayed(self):
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'wrongpassword'})
        #make sure login function is not called
        self.assertTrue(response.status_code == 200)
        # make sure form errors are displayed
        self.assertContains(response,'Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def test_user_login_GetRequest_RenderLoginForm(self):
        response = self.client.get(reverse('users:login'))

    def test_user_login_GetRequest_RenderLoginForm(self):
        response = self.client.get(reverse('users:login'))

        # make sure login form is rendered
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')