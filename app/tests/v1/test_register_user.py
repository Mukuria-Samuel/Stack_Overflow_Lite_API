import json
from .base_test import BaseTestCase

class TestRegister(BaseTestCase):
    def test_login(self):
        with self.client:
            response = self.client.post('/api/v1/auth/login',data=json.dumps(dict(
                    username='userman',
                    password='summertime2')),content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual("Logged in, welcome",result["message"])
            self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        with self.client:
            self.client.post('/api/v1/auth/register',data=json.dumps(dict(
                    username='userman',
                    password='summertime2',
                    role='attendant',
                    confirm_password='summertime2')),content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual(" {} : Added successfully",result["message"])
            self.assertEqual(response.status_code, 201)

    def test_invalid_username(self):
        with self.client:
            self.client.post('/api/v1/auth/register',data=json.dumps(dict(
                    username='///////',
                    password='summertime2',
                    role='attendant',
                    confirm_password='summertime2')),content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual("Invalid username",result["message"])
            self.assertEqual(response.status_code, 403)

    def test_double_registration(self):
        with self.client:
            self.client.post('/api/v1/auth/register',data=json.dumps(dict(
                    username='userman',
                    password='summertime2',
                    role='attendant',
                    confirm_password='summertime2')),content_type='application/json')
            result = json.loads(response.data)
            self.assertEqual("User already in system",result["message"])
            
    
    