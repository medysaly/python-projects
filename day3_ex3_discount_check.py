age = int(input('Enter your age: '))

if age < 12:
    adult = input('Are you with an adult? ').strip().lower()
    if adult == 'yes':
        print('Child ticket with adult: $5')
    else:
        print('Sorry, you must be with an adult.')

elif age > 12:
    student = input('Are you a student? ').lower().strip()
    if student == 'yes':
        print('Student ticket: $8')

    else:
        print('Regular ticket: $12')