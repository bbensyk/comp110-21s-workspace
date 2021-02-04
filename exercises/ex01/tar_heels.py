"""An exercise in remainders and boolean logic."""

__author__ = "730442945"


# Begin your solution here...
N: int = int(input("Enter an int"))
a: int = N % 2
b: int = N % 7

if a == 0 and b == 0:
    print("TAR HEELS")
else:
    if a == 0:
        print("TAR")
    else:
        if b == 0:
            print("Heels")
        else:
            print("CAROLINA")