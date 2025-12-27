import boto3 

# create the file and write content to it
with open ('mehditest.txt', 'w') as f:
    f.write('im mehdi, i will be a cloud engineer')


print ("File created successfully.")

# upload the file to S3 bucket

s3 = boto3.client('s3')

bucket_name = 'medy-cloud' 
s3.upload_file('mehditest.txt', bucket_name, 'mehditest.txt')   

print ("File uploaded successfully to S3 bucket.")

# Step 4: Download the file from S3
s3.download_file(bucket_name, 'test.txt', 'downloaded_test.txt')

print("✓ File downloaded from S3!")
print("\nCheck your folder - you should see:")
print("  - test.txt (original)")
print("  - downloaded_test.txt (from S3)")