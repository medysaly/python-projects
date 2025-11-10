#Create a dictionary of AWS storage prices 
# ("S3": 0.023, "Glacier": 0.004, "EFS": 0.08), 
# ask the user for a service name, and print the cost per GB.


storage_prices = {    "S3": 0.023,
    "Glacier": 0.004,
    "EFS": 0.08
}       

user_input = input("Enter the AWS storage service name (S3, Glacier, EFS): ")   
if user_input in storage_prices:
    print(f"The cost per GB for {user_input} is ${storage_prices[user_input]}")
else:
    print("Service not found. Please enter a valid AWS storage service name.")  