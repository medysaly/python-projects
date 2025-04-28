def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b) :
    return a / b

a = int(input('Enter a: '))
b = int(input('Enter B: '))
sign = input('Enter operator (+, -, *, /): ')

if sign == '+':
    print(add(a,b))

elif sign == '-':
    print(subtract(a,b))

elif sign == '*':
    print(multiply(a,b))

elif sign == '/':
    print(divide(a,b))

else:
    print('Invalid operator!')