import boto3

# Step 1: Create a text file
with open('test.txt', 'w') as f:
    f.write("Hello! This is my first AWS project.\n")
    f.write("I'm learning boto3!")

print("✓ File created!")

# Step 2: Upload to S3
s3 = boto3.client('s3')
bucket_name = 'medy-cloud'  # CHANGE THIS!

s3.upload_file('test.txt', bucket_name, 'test.txt')

print("✓ File uploaded to S3!")