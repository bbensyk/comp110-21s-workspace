"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730442945"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    fortune: int = randint(1,4)
    if fortune <3:
        if fortune == 1: 
            return("Man who runs behind car gets exhausted.")
        else:
            return("Man who runs infront of car gets tired.")
    else:
        if fortune == 4:
            return("Eat more fortune cookies.")
        else:
            return("Go to gym, delete facebook.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
