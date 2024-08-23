import unittest

from app.services.AuthService import AuthService


class TestAuthService(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.auth_service = AuthService()

    def test_Login_ValidData_SuccessAndTokenReturned(self):
        login_data = {
            'userName': 'admin',
            'password': '123'
        }

        result = self.auth_service.login(login_data)

        self.assertTrue(result.success)
        self.assertIsNotNone(result.token)

    def test_Login_InvalidPassword_TokenIsEmpty(self):
        login_data = {
            'userName': 'admin',
            'password': 'wrong_password'
        }

        result = self.auth_service.login(login_data)

        self.assertFalse(result.success)
        self.assertEqual('', result.token)

    def test_Login_InvalidUsername_TokenIsEmpty(self):
        login_data = {
            'userName': 'invalid_username',
            'password': '123'
        }

        result = self.auth_service.login(login_data)

        self.assertFalse(result.success)
        self.assertEqual('', result.token)

    def test_Login_MissingUsername_RaisesException(self):
        login_data = {
            'password': '123'
        }

        with self.assertRaises(Exception):
            self.auth_service.login(login_data)

    def test_Login_MissingPassword_RaisesException(self):
        login_data = {
            'userName': 'admin'
        }

        with self.assertRaises(Exception):
            self.auth_service.login(login_data)

    def test_VerifyToken_RegisteredToken_True(self):
        token = 'test_token'
        self.auth_service.tokens[token] = 'admin'

        result = self.auth_service.verify_token(token)

        self.assertTrue(result)

    def test_VerifyToken_UnregisteredToken_False(self):
        token = 'invalid_token'

        result = self.auth_service.verify_token(token)

        self.assertFalse(result)

    def test_GetUserName_ByRegisteredToken_UsernameReturned(self):
        token = 'test_token'
        user_name = 'admin'
        self.auth_service.tokens[token] = user_name

        result = self.auth_service.get_user_name(token)

        self.assertEqual(user_name, result)

    def test_GetUserName_ByUnregisteredToken_RaisesException(self):
        token = 'test_token'
        user_name = 'admin'
        self.auth_service.tokens[token] = user_name

        with self.assertRaises(Exception):
            self.auth_service.get_user_name('invalid_token')

    def test_AddToken_TokenWithUsername_TokenAddedToDictionary(self):
        token = 'test_token'
        user_name = 'admin'

        self.auth_service.add_token(token, user_name)

        self.assertEqual(1, len(self.auth_service.tokens))
        self.assertEqual(self.auth_service.tokens[token], user_name)
