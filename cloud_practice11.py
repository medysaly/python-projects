import boto3 

s3 = boto3.client('s3')

bucket_name = "mehdi-portfolio-website"

response = s3.list_objects_v2(Bucket=bucket_name)

for obj in response.get('Contents', []):
    file_name = obj['Key']
    s3.download_file(bucket_name, file_name, file_name)
    print(f'Downloaded: {file_name}')