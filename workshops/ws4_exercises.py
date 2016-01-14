# coding=utf-8


# Define a function my_max() that takes two numbers as arguments and returns the largest of them.
# Use the if-then-else construct available in Python.
# (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
def my_max(x, y):
    if x > y:
        return x
    else:
        return y


# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_tree(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z


# Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
def my_len(string):
    length = 0
    is_string_finished = False
    while not is_string_finished:
        try:
            string[length]
            length += 1
        except:
            is_string_finished = True
    return length


# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel,
# False otherwise.
def is_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if character in vowels:
        return True
    else:
        return False

# No. 5
# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
# That is, double every consonant and place an occurrence of "o" in between.
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".
def translate(text_to_translate):
    pass


# No. 6
# Define a function my_sum() and a function multiply() that sums and multiplies (respectively)
# all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10,
# and multiply([1, 2, 3, 4]) should return 24.
def my_sum(list_to_sum):
    sum_to_count = 0
    for number in list_to_sum:
        sum_to_count = sum_to_count + number
    return sum_to_count


def multiply(list_to_mulitiply):
    sum_of_multiply = 1
    for index in range(len(list_to_mulitiply)):
        sum_of_multiply = sum_of_multiply * list_to_mulitiply[index]
    return sum_of_multiply

# No. 7
# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

# No. 8
# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

# No. 9
# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a,
# and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)

# No. 10
# Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise. You may use your is_member() function, or the in operator,
# but for the sake of the exercise, you should (also) write it using two nested for-loops.
