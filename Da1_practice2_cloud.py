name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_student = input("Are you a student? (True/False): ").lower() == "true"
favorite_cloud = input("Enter your favorite cloud platform: ")

print(f"My name is {name}, I am {age} years old, and my favorite cloud platform is {favorite_cloud}. Am I a student? {is_student}")

