"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz"instead of the 
number and for multiples of five print "Buzz". 
For numbers which are multiples of both three and five 
print "FizzBuzz".

-Function
-Looping
-Multiple Conditionals
-Mathematical Operators
"""
def fizzbuzz(max_num):
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 != 0:
            print('Fizz')    
        elif num % 3 != 0 and num % 5 == 0:
            print('Buzz') 
        else:
            print('FizzBuzz')


fizzbuzz(101)
