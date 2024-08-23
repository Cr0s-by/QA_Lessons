import os
import subprocess
import unittest


class StorageTestCase(unittest.TestCase):
    external_app = 'storage.cmd'
    storage_path = './storage/users.dat'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        if not os.path.isdir('storage'):
            os.mkdir('storage')

    def setUp(self) -> None:
        super().setUp()
        if os.path.isfile(self.storage_path):
            os.remove(self.storage_path)

    def test_Create_NewUser_ValidUser(self):

        command = self.external_app + " create IvanIvanov"

        result = self.execute_shell(command)

        self.assertEqual("1", result)

        storage_content = self.read_storage()
        self.assertEqual('1  {}IvanIvanov\n', storage_content)

    def test_Create_UseOfAllowedSpecialCharactersInUserName_SpecialCharactersInTheUserName(self):
        command = self.external_app + " create IvanIvanov@#$%"

        result = self.execute_shell(command)

        self.assertEqual("1", result)

        storage_content = self.read_storage()
        self.assertEqual('1  {}IvanIvanov@#$%\n', storage_content)

    def test_Create_UseSpecialCharactersInUserName_SpecialCharactersInTheUserName(self):
        command = self.external_app + " create IvanIvanov!^&*()"

        result = self.execute_shell(command)

        self.assertEqual("1", result)

        storage_content = self.read_storage()
        self.assertEqual('1  {}IvanIvanov!^&*()\n', storage_content)

    def test_Create_UsingCyrillicCharactersToCreateAUserName_UserCreation(self):
        command = self.external_app + " create ПетрПетрович"

        result = self.execute_shell(command)

        self.assertEqual("1", result)

        storage_content = self.read_storage()
        self.assertEqual('1  {}ПетрПетрович\n', storage_content)

    def test_Create_EmptyUserName_UnableToCreateAnEmptyUser(self):
        command = self.external_app + " create "

        result = self.execute_shell(command)

        self.assertEqual("", result)

        storage_content = self.read_storage()
        self.assertEqual('', storage_content)

    def test_Create_CreateTwoUsers_UsersCreated(self):
        command_create = self.external_app + " create IvanIvanov"
        self.execute_shell(command_create)
        command_create = self.external_app + " create PetrPetrovich"
        self.execute_shell(command_create)

        storage_content = self.read_storage()
        self.assertEqual('1  {}IvanIvanov\n2  {}PetrPetrovich\n', storage_content)

    def test_Get_UseID_GetUserName(self):
        command_create = self.external_app + " create IvanIvanov"
        self.execute_shell(command_create)
        command_get = self.external_app + " get 1"
        result = self.execute_shell(command_get)

        self.assertEqual("IvanIvanov", result)

        storage_content = self.read_storage()
        self.assertEqual('1  {}IvanIvanov\n', storage_content)

    def test_Get_UseNegativeID_NoIdMessage(self):
        command_create = self.external_app + " create IvanIvanov"
        self.execute_shell(command_create)
        command_get = self.external_app + " get -1"
        result = self.execute_shell(command_get)

        self.assertEqual("No ID", result)

        storage_content = self.read_storage()
        self.assertEqual('IvanIvanov\n', storage_content)

    def test_Get_UseZeroID_NoIdMessage(self):
        command_create = self.external_app + " create IvanIvanov"
        self.execute_shell(command_create)
        command_get = self.external_app + " get 0"
        result = self.execute_shell(command_get)

        self.assertEqual("No ID", result)

        storage_content = self.read_storage()
        self.assertEqual('1  {}IvanIvanov\n', storage_content)

    def execute_shell(self, command):
        pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        res = pipe.stdout.read()
        pipe.stdout.close()
        pipe.wait(2)

        return res.decode('ASCII').lstrip().rstrip()

    def read_storage(self):
        f = open(self.storage_path, 'r')
        content = f.read()
        f.close()

        return content
