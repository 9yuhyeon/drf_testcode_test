from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.response import Response
from django.urls import reverse

# Create your tests here.
class SignUpTest(APITestCase):
    def test_signup(self):
        user_data = {
            "username":"tester",
            "password":"testpassword",
            "email":"test@test.com",
            "fullname":"kim"
        }
        response = self.client.post(reverse("UserView"), user_data)
        self.assertEqual(response.data['message'], "가입 완료!!")