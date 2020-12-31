""" 
Write a program that prints the numbers from 1 to 15
and for multiples of 3 print 'Fizz' instead of the number
and for the multiples of 5 print 'Buzz'.
"""


def classic_fizzbuzz():
    # Classic algorithm. Not the best solution.
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

classic_fizzbuzz()


def enhanced_fizzbuzz():
    # An enhanced version of the fizzbuzz algorithm that more easily maintainable and readable
    for i in range(1, 16):
        output = ""
        if i % 3 == 0: output += "fizz"
        if i % 5 == 0: output += "buzz"
        if output == "": output = i
        print(output)

enhanced_fizzbuzz()
