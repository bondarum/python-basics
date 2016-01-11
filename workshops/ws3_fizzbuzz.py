# Write a function that prints the integers from 1 to n where n is passed to the function parameter.
#
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# i.e fuzbuzz(15) will print out this:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz


def fiz_buzz_1(n):
    for i in xrange(1, n + 1):
        if i % 15 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0:
            print "Buzz"
        else:
            print i


def fizz_buzz_2(n):
    for i in range(1, n + 1):
        print "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i


fiz_buzz_1(100)
fizz_buzz_2(100)
