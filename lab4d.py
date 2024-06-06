#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca college'

num1 = 1500
num2 = 1.50

def first_five(string_var):
    first_five_chars = string_var[0:5]
    return first_five_chars


def last_seven(string_var):
    last_seven_chars = string_var[-7:]
    return last_seven_chars


def middle_number(number_var):
    middle_digits = str(number_var)[1] + str(number_var)[2]
    return middle_digits


def first_three_last_three(string_var1, string_var2):
    first_and_last_three = string_var1[0:3] + string_var2[-3:]
    return first_and_last_three


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))

