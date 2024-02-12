# age_guesser_app/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Person


class GetHumanAgeViewTestCase(TestCase):
    def setUp(self):
        self.person = Person(name='John', age=30)

    def test_get_human_age(self):
        # Make a POST request to the view with the name of the person
        response = self.client.post(reverse('get_human_age'), {'name': 'John'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the returned JSON data contains the correct age for the person we created
        self.assertEqual(response.json()['age'], self.person.age)

    def test_get_human_age_person_not_found(self):
        # Make a POST request to the view with a name that doesn't exist
        response = self.client.post(reverse('get_human_age'), {'name': 'Nonexistent'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the returned JSON data contains an error message
        self.assertIn('error', response.json())
