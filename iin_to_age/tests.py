from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {'iin': '680903402745'}
        response = self.client.post('http://127.0.0.1:8000/api/people/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
