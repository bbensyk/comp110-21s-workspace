"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730442945"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
a: int = int(randint(1,10))

print("Your fortune cookie says... ")

if a < 5:
    if a == 1:
        print("Does this seem real?")
    else:
        if a ==2:
         print("Look Behind you.")
        if a == 3:
         print("Are you real?")
        if a == 4:
            print("Don't trust anything.")
else: 
    if a == 5:
        print("Do you feel like you're being watched.")
    else:
        if a < 8: 
            if a == 6:
                print("I'll see you later.")
            else:
                print("NO ")
        if a < 10:
            if a == 8:
                print: "I am ready, are you?"
            if a == 9:
             print("666")
        else:
            print("Hi :)")
    
print("Now, go spread possitive vibes.")