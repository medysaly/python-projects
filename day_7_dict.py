phone_book = {
    "Alice": "123-4567",
    "Bob": "987-6543",
    "Charlie": "555-0000"
}

while True:
    name = input("Enter Name (or 'exit' to quit): ").strip().capitalize()

    if name.lower() == "exit":
        break

    if name in phone_book:
        print(f"{name}'s number is {phone_book[name]}")
    else:
        print("Name not found.")
        add_number = input(f"Enter a number for {name}: ")
        phone_book[name] = add_number
        print(f"{name} added to phone book.")






