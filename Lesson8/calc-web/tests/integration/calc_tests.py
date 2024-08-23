import json
import unittest
from app import application
from app.services.AuthService import AuthService
from configuration import TestConfig


class CalcTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        application.config.from_object(TestConfig)
        self.client = application.test_client()

        AuthService.tokens = {}

    def test_LoginAndCalc_SumOfNumbers_CorrectResult(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        calc_data = {
            "op1": "1",
            "op2": "2",
            "operation": "+"
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        token = login_response_data['data']['token']

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(200, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())
        self.assertEqual('success', calc_response_data['status'])
        self.assertIsNone(calc_response_data["message"])
        self.assertEqual(3, calc_response_data['data'])

    def test_LoginAndCalc_EmptyOperands_InvalidLiteral(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        calc_data = {
            "op1": "",
            "op2": "",
            "operation": "+"
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        token = login_response_data['data']['token']

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(500, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())
        self.assertEqual('error', calc_response_data['status'])
        self.assertEqual("Unknown error: invalid literal for int() with base 10: ''", calc_response_data["message"])
        self.assertIsNone(calc_response_data['data'])

    def test_LoginAndCalc_SameOperandSubtraction_ZeroValue(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        calc_data = {
            "op1": "1",
            "op2": "1",
            "operation": "-"
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        token = login_response_data['data']['token']

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(200, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())
        self.assertEqual('success', calc_response_data['status'])
        self.assertIsNone(calc_response_data["message"])
        self.assertEqual(0, calc_response_data['data'])

    def test_LoginAndCalc_AddingTheSameOperands_CorrectValue(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        calc_data = {
            "op1": "44",
            "op2": "44",
            "operation": "+"
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        token = login_response_data['data']['token']

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(200, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())
        self.assertEqual('success', calc_response_data['status'])
        self.assertIsNone(calc_response_data["message"])
        self.assertEqual(88, calc_response_data['data'])

    def test_LoginAndCalc_MultiplyOperation_UnknownOperation(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }
        calc_data = {
            "op1": "1",
            "op2": "2",
            "operation": "*"
        }

        login_response = self.client.post('/login', data=json.dumps(login_data), content_type='application/json')
        self.assertEqual(200, login_response.status_code)

        login_response_data = json.loads(login_response.get_data())
        token = login_response_data['data']['token']

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(200, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())
        self.assertEqual('fail', calc_response_data['status'])
        self.assertEqual("unknown operation", calc_response_data["message"])
        self.assertIsNone(calc_response_data['data'])

    def test_Calc_SumNumbersWithRegisteredToken_CorrectResult(self):
        token = '2b62-84fb'
        AuthService.add_token(token, 'test')

        calc_data = {
            "op1": "1",
            "op2": "2",
            "operation": "+"
        }

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(200, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())

        self.assertEqual('success', calc_response_data['status'])
        self.assertIsNone(calc_response_data["message"])
        self.assertEqual(3, calc_response_data['data'])

    def test_Calc_SumNumbersWithNotRegisteredToken_InvalidToken(self):
        access_token = '29f0c771-cd0b-4f0b-9f72-dce04c2acb0f'
        AuthService.add_token(access_token, 'frost')
        token = 'd8f7ff73-ab3c-432b-a382'

        calc_data = {
            "op1": "1",
            "op2": "2",
            "operation": "+"
        }

        calc_response = self.client.post('/calc', data=json.dumps(calc_data), content_type='application/json',
                                         headers={"X-Auth-Token": token})
        self.assertEqual(200, calc_response.status_code)

        calc_response_data = json.loads(calc_response.get_data())

        self.assertEqual('fail', calc_response_data['status'])
        self.assertEqual("invalid token", calc_response_data["message"])
        self.assertIsNone(calc_response_data['data'])
