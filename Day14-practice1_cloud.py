#Create a dictionary representing an EC2 instance (id, type, region) and print each key/value pair.

ec2_instance = {
    "id": "i-0abcd1234efgh5678",
    "type": "t2.micro",
    "region": "us-west-2"
}

print(f"The instance ID is: {ec2_instance['id']}")
print(f"The instance type is: {ec2_instance['type']}")
print(f"The instance region is: {ec2_instance['region']}")