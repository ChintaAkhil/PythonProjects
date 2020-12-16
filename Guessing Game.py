import random


def guess(n, name):
    random_number = random.randint(1, n)
    guess_number = 0
    while random_number != guess_number:
        guess_number = int(input(f"{name} please enter a number between 1 and {n} including {n} and excluding 1 : "))
        if guess_number > n:
            print(f"{name} guessed Number is out of range please enter a  number between 1 and {n} ")
        elif random_number > guess_number:
            print(f"{name} guessed Number is lower please enter a higher value ! ")
        elif random_number < guess_number:
            print(f"{name} guessed Number is Higher please enter a lesser value ! ")

    print(f"Congratulation {name} you've guessed the correct value !!!! Random number generated is {random_number}")


name = input("Please enter your name: ")
n = int(input("Please enter your maximum number: "))
guess(n, name)
