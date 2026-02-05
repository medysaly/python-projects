import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

if len(response['Reservations']) == 0:
    print("No EC2 instances found in your account")
else:
    print(f"Found {len(response['Reservations'])} EC2 instances")