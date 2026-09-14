import random

try:
    low = int(input("enter your low number:\n"))
    high = int(input("enter your high number:\n"))
except:
    print("ERROR : please enter a valid number")

r = random.randint(low, high)

guess_count = 5
while guess_count>0:
    try:
        new_guess = int(input(f" remaind : {guess_count }=> your guess:\n"))

        if r > new_guess :
            print("your number is small than r")
        elif r < new_guess:
            print("your number is big than r")
        else:
            print("GREAT")
            break
        guess_count -=1
    except:
        print("ERROR : please enter a valid number:\n")
