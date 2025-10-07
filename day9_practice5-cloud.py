def calculate_bill(amount, tax_rate):
    tax = amount * tax_rate
    total = amount + tax
    return total
user_amount = float(input("Enter the amount: "))
user_tax_rate = float(input("Enter the tax rate (as a decimal): "))
total_amount = calculate_bill(user_amount, user_tax_rate)

print(f"Total amount including tax: {total_amount}")
