import boto3

s3 = boto3.client('s3')

bucket_name = "mehdi-portfolio-website"

response = s3.list_objects_v2(Bucket=bucket_name)

file_count = 0
total_size = 0


print(f'Objects in S3 bucket: {bucket_name}')
print('-----------------------------------')

for obj in response.get('Contents', []):
    print(obj['Key'])
    file_count = file_count + 1
    total_size = total_size + obj['Size']

print('-----------------------------------')
print(f'Total number of files: {file_count}')
print(f'Total size of files: {total_size} bytes')