import boto3

s3 = boto3.client('s3')
bucket_name = "mehdi-cloud-2"
s3.delete_object(Bucket=bucket_name, Key='one.png')
response = s3.list_objects_v2(Bucket=bucket_name)


print(f'Objects in S3 bucket: {bucket_name}')
print('-----------------------------------')   
for obj in response.get('Contents', []):
    print(obj['Key'])



