def greet_user(name, cloud):
    return f"Hello, {name}! Welcome to the {cloud} cloud."

name = input("Enter your name: ")
cloud = input("Enter your favorite cloud service (e.g., AWS, Azure, GCP): ")
message = greet_user(name, cloud)
print(message)