import unittest

from workshops.ws4_exercises import my_max, max_of_tree, my_len, is_vowel, my_sum, multiply, reverse, is_palindrome, \
    is_member, overlapping, translate


class TestPythonFunctions(unittest.TestCase):
    def test_max_function_should_return_largest_given_number(self):
        self.assertEqual(my_max(1, 2), 2)
        self.assertEqual(my_max(4, 3), 4)

    def test_max_of_tree_function_should_return_largest_given_number(self):
        self.assertEqual(max_of_tree(1, 2, 3), 3)
        self.assertEqual(max_of_tree(4, 6, 5), 6)
        self.assertEqual(max_of_tree(9, 8, 7), 9)

    def test_is_vowel_function_should_true_if_given_character_is_vowel(self):
        self.assertTrue(is_vowel('a'))
        self.assertFalse(is_vowel('b'))

    def test_my_sum_function_should_sum_given_numbers_in_list(self):
        self.assertEqual(my_sum([1, 2, 3]), 6)
        self.assertEqual(my_sum([1, 10, 9]), 20)

    def test_multiply_function_should_multiply_given_numbers_in_list(self):
        self.assertEqual(multiply([2, 2, 3]), 12)
        self.assertEqual(multiply([100, 1]), 100)
        self.assertEqual(multiply([15, 2, 4]), 120)

    def test_reverse_function_should_return_reversed_string(self):
        self.assertEqual(reverse('I am learning python'), 'nohtyp gninrael ma I')
        self.assertEqual(reverse('Mateusz is a great trainer'), 'reniart taerg a si zsuetaM')

    def test_is_palindrome_function_should_return_true_if_given_string_is_palindrome(self):
        self.assertTrue(is_palindrome('level'))
        self.assertTrue(is_palindrome('noon'))
        self.assertFalse(is_palindrome('kasamdasak'))

    def test_is_member_function_should_return_true_if_given_value_is_member_of_given_list(self):
        self.assertTrue(is_member('member', [1, 'asd', 123, 'member']))
        self.assertFalse(is_member(1234, [1, 'asd', 123, 'member']))

    def test_overlapping_function_should_true_if_given_lists_are_overlapping_each_other(self):
        self.assertTrue(overlapping([1, 'asd', 123, 'member'], ['asd', 123]))
        self.assertTrue(overlapping([1, 'asd', 123, 'member'], ['member', ]))
        self.assertFalse(overlapping([1, 'asd', 123, 'member'], ['member2']))

    def test_translate_function_should_translate_string_into_robbers_language(self):
        self.assertEqual(translate("this is fun"), "tothohisos isos fofunon")

    def test_my_len_function_should_return_expected_length_of_string(self):
        self.assertEqual(my_len('test'), 4)
        self.assertEqual(my_len('some sentence'), 13)
        self.assertEqual(my_len(''), 0)
        self.assertEqual(my_len('!@#$%^&*()'), 10)

if __name__ == '__main__':
    unittest.main()
