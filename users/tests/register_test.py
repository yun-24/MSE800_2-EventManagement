from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from unittest.mock import patch

class UserRegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('users.views.UserCreationForm')
    @patch('users.views.login')
    def test_user_register_ValidForm_UserCreatedAndLoggedIn(self, mock_login, mock_form):
        # Mock the form to return valid data
        mock_form_instance = mock_form.return_value
        mock_form_instance.is_valid.return_value = True
        mock_form_instance.save.return_value = User(username='testuser')

        # Make a POST request to the register view
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })

        # Ensure the form is called with the POST data
        mock_form.assert_called_once_with(response.wsgi_request.POST)  # Adjusted here

        # Ensure the form's save method is called
        mock_form_instance.save.assert_called_once()

        # Ensure the login function is called with the correct user
        mock_login.assert_called_once_with(response.wsgi_request, mock_form_instance.save.return_value)

        # Ensure the user is redirected to the event list page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('events:event_list'))

    @patch('users.views.UserCreationForm')
    def test_user_register_InvalidForm_FormErrorsDisplayed(self, mock_form):
        # Mock the form to return invalid data
        mock_form_instance = mock_form.return_value
        mock_form_instance.is_valid.return_value = False

        # Make a POST request to the register view
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'wrongpassword',
        })

        # Ensure the form is called with the POST data
        mock_form.assert_called_once_with(response.wsgi_request.POST)  # Adjusted here

        # Ensure the form is not saved
        mock_form_instance.save.assert_not_called()

        # Ensure the response status code is 200 (form errors are displayed)
        self.assertEqual(response.status_code, 200)

    def test_user_register_GetRequest_RenderRegisterForm(self):
        # Make a GET request to the register view
        response = self.client.get(reverse('users:register'))

        # Ensure the register form is rendered
        self.assertContains(response, 'Register')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')
        self.assertContains(response, 'Password confirmation')