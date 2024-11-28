# Problem 1: Check if a number is even or odd
# This program takes an integer input from the user and checks whether the number is even or odd using the modulus operator.
number = int(input('Enter the number : '))
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')


# Problem 2: Calculate the summation of numbers from 1 to a given positive number
# This program prompts the user to enter a positive number and calculates the sum of all integers from 1 to that number.
number = int(input("Enter a positive number : "))
summition = 0
if number < 0:
    print("Enter a positive number")
else:
    for i in range(1, number + 1):
        summition += i
    print(f'The summition from 1 to {number} is {summition}')


# Problem 3: Calculate the factorial of a given number
# This program calculates the factorial of a given number using a while loop.
number = int(input('Enter the number : '))
if number < 0:
    print('Enter a positive number!')
else:
    multi = 1
    start = 1
    end = number
    while start <= end:
        multi *= start
        start += 1
    print(f'The factorial of {number} is {multi}')


# Problem 4: Reverse a string
# Method 1: Reverse a string using slicing
# This program takes a string input from the user and reverses it using Python slicing.
string = input('Enter the string : ')
string = string[::-1]
print(f'The reverse string is {string}')

# Method 2: Reverse a string using a loop
# This program reverses a string by iterating through it in reverse order and building a new string character by character.
string = input('Enter the string : ')
new_string = ''
for i in range(len(string) - 1, -1, -1):
    new_string += string[i]
print(f'The reverse string is {new_string}')


# Problem 5: Check if a string is a palindrome
# This program defines a function to check if a given string is a palindrome, then uses that function to determine if the input string reads the same forward and backward.
def is_palindrome(string):
    return string == string[::-1]

string = input('Enter the string : ')
print(is_palindrome(string))
