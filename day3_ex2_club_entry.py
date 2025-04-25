# Ask the user for their age
# Ask the user if they have an ID (yes or no)
# If they are 18 or older AND they have an ID,
# print "You can enter the club!"
# Otherwise, print "Sorry, you cannot enter."

age = int(input('Enter your age: '))
id = input('Do you have an ID: ').title().strip()

if age >= 18 and id == 'Yes':
    print('You can Enter the club! ')

else:
    print('Sorry, you cannot enter.')

