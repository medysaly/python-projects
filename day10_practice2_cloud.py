def calculate_storage_cost(gb, price_per_gb=0.023):
       return gb * price_per_gb

user_gb = int(input("Enter the amount of storage in GB: "))
user_cost = calculate_storage_cost(user_gb, price_per_gb=0.023) 

print(f"the cost of the storage is {user_cost}.")