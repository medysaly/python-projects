score = int(input('Enter your score: '))

if 90 <= score <= 100:
    print('You got an A!')

elif 80 <= score <= 89:
    print('You got a B!')

elif 70 <= score <= 79:
    print('You got a C!')

elif 60 <= score <= 69:
    print('You got a D!')

elif score < 60:
    print('You got a F!')

else:
    print('Please enter the correct number.')