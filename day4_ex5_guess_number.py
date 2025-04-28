import random

# Generate the random number ONCE
ran_num = random.randint(1, 10)

while True:
    guess = int(input('Guess a number (1-10): '))  # convert input to integer
    if guess == ran_num:
        print('Congratulations!')
        break  # Exit the loop when correct
    elif guess > ran_num:
        print('Too high! Guess again.')
    else:
        print('Too low! Guess again.')