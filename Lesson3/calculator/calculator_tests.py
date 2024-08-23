import os
import subprocess
import unittest


class CalculatorTestCase(unittest.TestCase):
    external_app = 'math.cmd'
    log_path = './logs/math.log'

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        if not os.path.isdir('logs'):
            os.mkdir('logs')

    def setUp(self) -> None:
        super().setUp()
        if os.path.isfile(self.log_path):
            os.remove(self.log_path)

    def test_Add_Positives_ValidPositive(self):

        # arrange
        command = self.external_app + " add 1 2"

        # act
        res = self.execute_shell(command)

        # assert
        self.assertEqual(3, int(res))

        log_content = self.read_log()
        self.assertEqual("add operation\nfirst param: 1\nsecond param: 2\n", log_content)

    def test_Add_Negatives_ValidNegative(self):

        # arrange
        command = self.external_app + " add -1 -2"

        # act
        res = self.execute_shell(command)

        # assert
        self.assertEqual(-3, int(res))

        log_content = self.read_log()
        self.assertEqual("add operation\nfirst param: -1\nsecond param: -2\n", log_content)

    def execute_shell(self, command):
        pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        res = pipe.stdout.read()
        pipe.stdout.close()
        pipe.wait(10)

        return res

    def read_log(self):
        f = open(self.log_path, 'r')
        content = f.read()
        f.close()

        return content
