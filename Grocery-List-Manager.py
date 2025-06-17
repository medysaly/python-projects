grocery_list = ['potatoes', 'tomatoes', 'onions', 'carrots', 'spinach']
print("Welcome to the Grocery List Manager!")
add_item = input("Enter 1 to add an item, 2 to remove an item, or 3 to view the list: ")
if add_item == '1':
    item_to_add = input("Enter the item you want to add: ")
    grocery_list.append(item_to_add)
    print(f"{item_to_add} has been added to your grocery list.")

elif add_item == '2':
    item_to_remove = input("Enter the item you want to remove: ")
    if item_to_remove in grocery_list:
        grocery_list.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from your grocery list.")
    else:
        print(f"{item_to_remove} is not in your grocery list.")
elif add_item == '3':
    print("Your grocery list contains the following items:")
    for item in grocery_list:
        print(f"- {item}")
else:
    print("Invalid option. Please enter 1, 2, or 3.")