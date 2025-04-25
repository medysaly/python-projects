# Ask the user for their age
# Ask if the user is a student (yes or no)
# If they are younger than 18 OR they are a student,
# print "You get a discount!"
# Otherwise, print "No discount, sorry."

age = int(input('Enter your age: '))
student = input('Are you a student? ').lower().strip()

if age < 18 or student == 'yes':
    print('You get a discount! ')

else:
    print('No discount, sorry.')