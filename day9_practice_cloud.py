def is_even(num):
    return num % 2 == 0

user_input = int(input("Enter a number: "))
if is_even(user_input):
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")
