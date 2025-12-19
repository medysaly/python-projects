import re 
username = "mehdi_1234567890"

result = re.match(r"mehdi", username)

if result:
    print("The username starts with 'mehdi'")
else:
    print("The username does not start with 'mehdi'")