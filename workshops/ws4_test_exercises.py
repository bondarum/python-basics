import unittest

from workshops.ws4_exercises import my_max, max_of_tree, my_len, is_vowel, my_sum, multiply


class TestPythonFunctions(unittest.TestCase):
    def test_max_function_should_return_largest_given_number(self):
        self.assertEqual(my_max(1, 2), 2)
        self.assertEqual(my_max(4, 3), 4)

    def test_max_of_tree_function_should_return_largest_given_number(self):
        self.assertEqual(max_of_tree(1, 2, 3), 3)
        self.assertEqual(max_of_tree(4, 6, 5), 6)
        self.assertEqual(max_of_tree(9, 8, 7), 9)

    def test_my_len_function_should_return_expected_length_of_string(self):
        self.assertEqual(my_len('test'), 4)
        self.assertEqual(my_len('some sentence'), 13)
        self.assertEqual(my_len(''), 0)
        self.assertEqual(my_len('!@#$%^&*()'), 10)

    def test_is_vowel_function_should_true_if_given_character_is_vowel(self):
        self.assertTrue(is_vowel('a'))
        self.assertFalse(is_vowel('b'))

    def test_my_sum_function_should_sum_given_numbers_in_list(self):
        self.assertEqual(my_sum([1, 2, 3]), 6)
        self.assertEqual(my_sum([1, 10, 9]), 20)

    def test_multiply_function_should_multiply_given_numbers_in_list(self):
        self.assertEqual(multiply([2, 2, 3]), 12)
        self.assertEqual(multiply([100, 1]), 100)

if __name__ == '__main__':
    unittest.main()
