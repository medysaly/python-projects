import boto3

s3 = boto3.client('s3')

bucket_name = 'mehdi-portfolio-website'

response = s3.list_objects_v2(Bucket = bucket_name )



print(f'Files in bucket: {bucket_name}')
print('-' * 40)


for obj in response['Contents']:
    print(f"  - {obj['Key']}")