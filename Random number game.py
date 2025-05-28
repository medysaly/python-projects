import random

num = random.randint(1,10)



while True:
    guess = int(input('Guess a number between 1 and 10 : '))
    if num == guess:
        print("correct!")
        break

    elif num > guess:
        print("higher guess again:")


    elif num < guess:
        print('Lower guess again')


    else:
        print("enter correct number")


