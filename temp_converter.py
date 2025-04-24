temp = float(input('Please enter temperature in Fahrenheit : '))

celsius = (temp - 32) * 5 / 9
c = round(celsius)

if celsius < 10:
    print(f'That\'s {c} - Freezing! 🥶' )

elif 10 <= celsius <= 30:
    print(f'Tha\'s {c} - Nice day! ☀️')

elif celsius > 30:
    print(f'That\'s {c} -It\'s hot outside! 🔥')

else:
    print('Please enter the right temperature')