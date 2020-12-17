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
    print(f"Congratulations {name} computer guessed your {number} !!!!")


name = input("Please enter your name: ")
computer_guess(name)
