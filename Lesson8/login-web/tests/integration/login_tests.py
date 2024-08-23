import json
import unittest

from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig


class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        application.config.from_object(TestConfig)
        self.client = application.test_client()

        AuthService.tokens = {}

    def test_Login_ValidUser_LoginSuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('success', response_data['status'])
        self.assertIsNotNone(response_data['data']['token'])

    def test_Login_InvalidUser_LoginFail(self):
        login_data = {
            'userName': 'fake-user',
            'password': 'fake-password'
        }

        response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])

    def test_LoginAndGetGreeting_ValidUserAndToken_GreetingGenerated(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        token = login_response_data['data']['token']

        greeting_response = self.client.get('/greeting', headers={'x-auth-token': token})
        self.assertEqual(200, greeting_response.status_code)

        greeting_response_data = json.loads(greeting_response.get_data())
        self.assertEqual('success', greeting_response_data['status'])
        self.assertIsNotNone(greeting_response_data['data'])
        self.assertEqual('Welcome, admin!', greeting_response_data['data'])

    def test_GetGreeting_ValidToken_GreetingGenerated(self):
        token = '123456'
        AuthService.add_token(token, 'Vasya')

        response = self.client.get('/greeting', headers={'x-auth-token': token})
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('success', response_data['status'])
        self.assertIsNotNone(response_data['data'])
        self.assertEqual('Welcome, Vasya!', response_data['data'])

    def test_GetGreeting_InvalidToken_FailGetGreeting(self):
        token = '123456'

        response = self.client.get('/greeting', headers={'x-auth-token': token})
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.get_data())
        self.assertEqual('fail', response_data['status'])
        self.assertIsNone(response_data['data'])

