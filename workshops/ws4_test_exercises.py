import unittest

from workshops.ws4_exercises import my_max


class TestPythonFunctions(unittest.TestCase):
    def test_max_function_should_return_largest_given_number(self):
        self.assertEqual(my_max(1, 2), 2)


if __name__ == '__main__':
    unittest.main()
