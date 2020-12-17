import random


def computer_guess(name):
    print("Please enter the number to be guessed by the computer:")
    x = int(input())
    low = 1
    high = x
    result = ''
    while result != 'c':
        if low != high:
            number = random.randint(low, high)
        else:
            number = low
        result = input(f"Is {number} or too High (H) ,or too Low (L) , or Correct (C)".lower())
        if result == 'h':
            high = number - 1
        elif result == 'l':
            low = number + 1
    print(f"Congratulations {name} computer guessed your number {number} correctly")


def guess(name):
    n = int(input("Please enter the maximum value: "))
    random_number = random.randint(1, n)
    guess_number = 0
    while random_number != guess_number:
        guess_number = int(input("Please enter the Guessed number: "))
        if guess_number > n:
            print(f"{name} guessed Number is out of range. Please enter a  number between 1 and {n} ")
        elif guess_number > random_number:
            print(
                f"{name} guessed number is higher than the randomly generated number, try with a lower value number: ")
        elif guess_number < random_number:
            print(
                f"{name} guessed number is lower than the randomly generated number, try with a higher value number: ")

    print(f"{name} the number you've guessed is same as the randomly generated number. Congratulations {name} .")


def switch(i):
    if i == 1:
        guess(name)
    if i == 2:
        computer_guess(name)


name = input("Please enter your name: ")
i = int(input("Please choose '1' to play the game where you've to guess the random number. \nPlease choose '2' to play "
              "the game where computer guesses the random number you've entered.\n"))
switch(i)
